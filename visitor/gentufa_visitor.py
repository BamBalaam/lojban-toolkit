import json
import sys
sys.path.append('.')

from parsimonious.grammar import NodeVisitor

from dictionary import Jbovlaste
from grammar_parser import Gentufa
from visitor import visitor_functions


def add_functions_as_methods(functions):
    # Decorator which dynamically adds a list of functions to a class,
    # to avoid overburdening its definition and separate class functions
    # into standalone files
    def decorator(Class):
        for function in functions:
            setattr(Class, function.__name__, function)
        return Class

    return decorator

@add_functions_as_methods(visitor_functions.functions)
class GentufaVisitor(NodeVisitor):

    def __init__(self, parse_tree):
        self.dictionary = Jbovlaste()
        self.output = {"sentence": parse_tree.full_text.replace(" EOL", ""), "segments": []}
        self.visit(parse_tree)

    def get_output(self):
        return self.output

    def get_json_output(self):
        return json.dumps(self.output)

    def generic_visit(self, node, visited_children):
        """The generic visit method."""
        return visited_children or node


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: gentufa_visitor.py [sentence to parse]")
        sys.exit(1)
    parse_tree = Gentufa().get_parsed_sentence(sys.argv[1])
    visitor = GentufaVisitor(parse_tree)
    try:
        print(visitor.get_json_output())
    except:
        print("Error:")