from parsimonious.expressions import Literal
from parsimonious.grammar import RuleVisitor
from parsimonious.nodes import Node

from parser.gentufa import Gentufa
from dictionary.jbovlaste import Jbovlaste


class GentufaVisualisor(RuleVisitor):

    def __init__(self, text):
        self.dictionary = Jbovlaste()
        print(text)
        self.ast = Gentufa().get_parsed_sentence(text)
        self.generic_visit(self.ast, [])
    
    def visit_MI(self, node, visited_children):
        return "I/me, we/us "
 
    def visit_SENTENCE(self, node, visited_children):
        output = {}
        for child in visited_children:
            output.update(child[0])
        return output

    def generic_visit(self, node, visited_children):
        return visited_children or node
