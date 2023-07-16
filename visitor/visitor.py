from parsimonious.grammar import RuleVisitor
from parsimonious.nodes import rule

from parsimonious.expressions import Quantifier, Sequence, OneOf, Regex

from parser.gentufa import Gentufa
from dictionary.jbovlaste import Jbovlaste


class GentufaVisitor(RuleVisitor):

    def __init__(self, text):
        self.sentence = ""
        self.dictionary = Jbovlaste()
        self.ast = Gentufa().get_parsed_sentence(text)
        self.visit(self.ast)

    def visit_MI(self, node, visited_children):
        return "I/me, we/us "

    def visit_DO(self, node, visited_children):
        return "You "

    def visit_RE(self, node, visited_children):
        return "2"

    def visit_CI(self, node, visited_children):
        return "3"

    def visit_PI(self, node, visited_children):
        return "."

    def visit_PA(self, node, visited_children):
        return "1"

    def visit_VO(self, node, visited_children):
        return "4"

    def visit_MU(self, node, visited_children):
        return "5"

    def visit_KI_O(self, node, visited_children):
        return ","

    def visit_NI_U(self, node, visited_children):
        return "-"

    def visit_space(self, node, visited_children):
        return " "

    def visit_SENTENCES(self, node, visited_children):
        #import pdb; pdb.set_trace()
        #for item in node.children:
        pass

    def visit_GISMU(self, node, visited_children):
        # import pdb; pdb.set_trace()
        pass

    def visit_POSSIBLE_GISMU(self, node, visited_children):
        self.sentence += self.dictionary.get_word(node.text)['glosswords'][0]['word'] + " "

    def generic_visit(self, node, visited_children):
        pass
