import sys

import xml.etree.ElementTree as ET


class Jbovlaste:
    """
    Class objects allow to grep words in the official Jbovlaste ("dictionary" in Lojban).
    Words include a type, definition, and optional glosswords in the target language of the dictionary.
    """

    def __init__(self, language="en"):
        self.dictionary = {}

        tree = ET.parse(f"./dictionary/jbovlaste-{language}.xml")
        root = tree.getroot()
        words = root[0].findall("valsi")

        for word in words:
            valsi = word.attrib["word"]
            valsi_type = word.attrib["type"]
            if valsi_type not in self.dictionary.keys():
                self.dictionary[valsi_type] = {}

            self.dictionary[valsi_type][valsi] = {}
            self.dictionary[valsi_type][valsi]["definition"] = word.find("definition").text
            self.dictionary[valsi_type][valsi]["glosswords"] = []
            glosswords = word.findall("glossword")
            for element in glosswords:
                glossword = element.attrib["word"]
                sense = None
                try:
                    sense = element.attrib["sense"]
                except Exception:
                    pass
                self.dictionary[valsi_type][valsi]["glosswords"].append(
                    {
                        "word": glossword,
                        "sense": sense,
                    }
                )

    def get_dict(self):
        return self.dictionary

    def get_word(self, word):
        word_struct = None
        for valsi_type in self.dictionary.keys():
            try:
                word_struct = self.dictionary[valsi_type][word]
                word_struct["type"] = valsi_type
            except KeyError:
                pass
        if word_struct is None:
            raise Exception("Word not found in the jbovlaste.")
        return word_struct

    def get_word_pretty(self, word):
        output_word = self.get_word(word)
        pretty_string = f"{word}\n\n"
        pretty_string += f"Word Type: {output_word['type']}\n"
        pretty_string += f"Definition: {output_word['definition']}\n"
        if len(output_word["glosswords"]) != 0:
            pretty_string += "Glossary Words:\n"
            for glossword in output_word["glosswords"]:
                pretty_string += f"\t- {glossword}\n"
        return pretty_string


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: jbovlaste.py [word to search in dict]")
        sys.exit(1)
    temporary_dict = Jbovlaste()
    print(temporary_dict.get_word_pretty(sys.argv[1]))
