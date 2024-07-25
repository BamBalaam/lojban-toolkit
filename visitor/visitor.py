from parsimonious.grammar import NodeVisitor

from dictionary import Jbovlaste
from grammar_parser import Gentufa
from visitor import visitor_functions
from .helpers import add_functions_as_methods


@add_functions_as_methods(visitor_functions.functions)
class GentufaVisitor(NodeVisitor):

    def __init__(self, text):
        self.dictionary = Jbovlaste()
        self.ast = Gentufa().get_parsed_sentence(text)
        self.output = {"sentence": text, "segments" : []}
        print(self.ast)
        self.visit(self.ast)

    def get_output(self):
        return self.output

    def generic_visit(self, node, visited_children):
        """ The generic visit method. """
        return visited_children or node
