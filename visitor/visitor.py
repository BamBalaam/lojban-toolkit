from parsimonious.grammar import NodeVisitor

from dictionary import Jbovlaste
from parser.gentufa import Gentufa
from visitor.helpers import pronouns_definition


class GentufaVisitor(NodeVisitor):

    def __init__(self, text):
        self.dictionary = Jbovlaste()
        self.ast = Gentufa().get_parsed_sentence(text)
        self.output = {"sentence": text, "segments" : []}
        print(self.ast)
        self.visit(self.ast)

    def get_output(self):
        return self.output

    def visit_SENTENCE(self, node, visited_children):
        for child in visited_children[0]:
            self.output["segments"].append(child)
        return

    def visit_LOJBAN_WORDS_OR_EXPRESSIONS(self, node, visited_children):
        return visited_children[0]

    def visit_PRONOUNS(self, node, visited_children):
        literal = visited_children[0][0].text
        return {
            literal: {"definition": pronouns_definition[literal], "type": "cmavo (pronoun)"}
        }

    def visit_BRIVLA(self, node, visited_children):
        return visited_children[0]

    def visit_BRIVLA_WITH_OR_WITHOUT_MODIFIERS(self, node, visited_children):
        return visited_children[0]

    def visit_BRIVLA_WITH_CU(self, node, visited_children):
        node_text = node.text.strip()
        return {
            node_text: {
                "type": "brivla with cu separator",
                "segments": [
                    {
                        "cu": {"definition": "selbri separator", "type": "cmavo"}
                    },
                    visited_children[2][0]
                ]
            }
        }

    def visit_GISMU(self, node, visited_children):
        literal = visited_children[0][0].text
        return {
            literal: self.dictionary.get_word_struct(literal)
        }

    def visit_NAMED_ENTITY(self, node, visited_children):
        node_text = node.text.strip()
        return {
            node_text: {"type": "named entity"}
        }

    def generic_visit(self, node, visited_children):
        """ The generic visit method. """
        return visited_children or node
