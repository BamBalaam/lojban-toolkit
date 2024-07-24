import os
import re
import sys

from parsimonious.grammar import Grammar

from dictionary.jbovlaste import Jbovlaste

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


class Gentufa:
    """
    TODO: Add docstring
    TODO: Add error handling
    """

    def __init__(self):
        dictionary = Jbovlaste().get_whole_dict()
        with open(os.path.join(__location__, "gerna.peg"), "r") as f:
            grammar_text = f.read()
        # Augment grammar text with dictionary words
        tags = re.findall(r"\{\{(.*?)\}\}", grammar_text)
        for tag in tags:
            words = '" / "'.join(dictionary[tag].keys())
            words = '"' + words + '"\n' # this join method doesn't add the initial double quotes
            grammar_text = grammar_text.replace("{{{{{0}}}}}".format(tag), words) # replace tag with dictionary words
        self.grammar = Grammar(grammar_text)

    def get_parsed_sentence(self, sentence):
        sentence = sentence + " EOL" # Adding end of line indicator to avoid parsing issues
        return self.grammar.parse(sentence)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: gentufa.py [sentence to parse]")
        sys.exit(1)
    parser = Gentufa()
    print(parser.get_parsed_sentence(sys.argv[1]))
