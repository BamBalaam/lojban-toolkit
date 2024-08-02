import os
import re
import sys

import xml.etree.ElementTree as ET

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


class Jbovlaste:
    """
    Creates an object which allows to fetch Lojban words.
    Gathers all words by parsing an XML export of the official
    La Jbovlaste ("dictionary" in Lojban).
    Words include:
        - a type
        - a definition
        - optional glossary words in the target language of the dictionary
    """

    def __init__(self, language="en"):
        self._dictionary = {}
        try:
            tree = ET.parse(os.path.join(__location__, f"jbovlaste-{language}.xml"))
        except FileNotFoundError as exc:
            raise ValueError(f"Language '{language}' is not available.") from exc
        root = tree.getroot()
        words = root[0].findall("valsi")

        for word in words:
            valsi, valsi_type = word.attrib["word"], word.attrib["type"]

            if valsi_type not in self._dictionary.keys():
                self._dictionary[valsi_type] = {}

            self._dictionary[valsi_type][valsi] = {}
            self._dictionary[valsi_type][valsi]["definition"] = word.find(
                "definition"
            ).text

            self._dictionary[valsi_type][valsi]["glosswords"] = []
            glosswords = word.findall("glossword")
            for element in glosswords:
                glossword = element.attrib["word"]
                sense = element.attrib.get("sense")
                self._dictionary[valsi_type][valsi]["glosswords"].append(
                    {
                        "word": glossword,
                        "sense": sense,
                    }
                )

    def get_whole_dict(self):
        return self._dictionary

    def get_word_struct(self, word):
        word_struct = None
        for valsi_type, words in self._dictionary.items():
            try:
                word_struct = words[word]
                word_struct["type"] = valsi_type
            except KeyError:
                pass
        if word_struct is None:
            raise KeyError("Word not found in the jbovlaste.")
        return word_struct

    def get_word_pretty(self, word):
        output_word = self.get_word_struct(word)
        pretty_string = f"{word}\n\n"
        pretty_string += f"Word Type: {output_word['type']}\n"
        pretty_string += f"Definition: {output_word['definition']}\n"
        if len(output_word["glosswords"]) != 0:
            pretty_string += "Glossary Words:\n"
            for glossword in output_word["glosswords"]:
                if glossword["sense"] is None:
                    pretty_string += f"\t- {glossword['word']}\n"
                else:
                    pretty_string += f"\t- {glossword['word']}"
                    pretty_string += f" (Sense: {glossword['sense']})\n"
        return pretty_string

    def decompose_definition(self, definition):
        arguments = re.findall(r"\$.*?\$", definition)
        return {"definition": definition, "max_args": len(arguments), "args": arguments}

    def get_definition_objects_list(self, word):
        definition = self.get_word_struct(word)["definition"]
        definitions_raw = definition.split(";")
        definitions_final = []
        for element in definitions_raw:
            definitions_final.append(self.decompose_definition(element))
        return definitions_final


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: jbovlaste.py [word to search in dict]")
        sys.exit(1)
    temporary_dict = Jbovlaste()
    try:
        print(temporary_dict.get_word_pretty(sys.argv[1]))
    except KeyError as e:
        print("Error: " + str(e))
        sys.exit(1)
