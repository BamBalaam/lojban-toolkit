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

    def __init__(self, text):
        self.dictionary = Jbovlaste()
        self.ast = Gentufa().get_parsed_sentence(text)
        self.output = {"sentence": text, "segments": []}
        print(self.ast)
        self.visit(self.ast)

    def get_output(self):
        return self.output

    def generic_visit(self, node, visited_children):
        """The generic visit method."""
        return visited_children or node
