import os
import sys

from parsimonious.grammar import Grammar

# from parsimonious.nodes import NodeVisitor

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


class Gentufa:
    """
    TODO: Add docstring
    TODO: Add error handling
    """

    def __init__(self):
        with open(os.path.join(__location__, "gerna.peg"), "r") as f:
            grammar_text = f.read()
        self.grammar = Grammar(grammar_text)

    def get_parsed_sentence(self, sentence):
        return self.grammar.parse(sentence)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: gentufa.py [sentence to parse]")
        sys.exit(1)
    parser = Gentufa()
    print(parser.get_parsed_sentence(sys.argv[1]))
