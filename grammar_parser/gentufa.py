import os
import re
import sys
sys.path.append('.')

from parsimonious.exceptions import IncompleteParseError, ParseError
from parsimonious.grammar import Grammar

from dictionary import Jbovlaste

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
            words = dictionary[tag].keys()
            replacement_to_tag = ""
            for word in words:
                replacement_to_tag += f'( "{word}" _ ) / '
            # clear last element adding an unused "/ "
            replacement_to_tag = replacement_to_tag[:-3]
            # replace tag with dictionary words
            grammar_text = grammar_text.replace(
                "{{{{{0}}}}}".format(tag), replacement_to_tag
            )
        self.grammar = Grammar(grammar_text)

    def get_parsed_sentence(self, sentence):
        sentence = (
            sentence + " EOL"
        )  # Adding end of line indicator to avoid parsing issues
        return self.grammar.parse(sentence)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: gentufa.py [sentence to parse]")
        sys.exit(1)
    parser = Gentufa()
    try:
        print(parser.get_parsed_sentence(sys.argv[1]))
    except (IncompleteParseError, ParseError) as exc:
        print("Error:", exc)