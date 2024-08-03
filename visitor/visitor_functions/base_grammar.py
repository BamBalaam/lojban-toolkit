__all__ = [
    "visit_BRIVLA",
    "visit_BRIVLA_WITH_OR_WITHOUT_MODIFIERS",
    "visit_GISMU",
    "visit_LOJBAN_WORDS_OR_EXPRESSIONS",
    "visit_SENTENCE",
]


def visit_SENTENCE(self, node, visited_children):
    for child in visited_children[0]:
        self.output["segments"].append(child)
    return


def visit_LOJBAN_WORDS_OR_EXPRESSIONS(self, node, visited_children):
    return visited_children[0]


def visit_BRIVLA(self, node, visited_children):
    return visited_children[0]


def visit_BRIVLA_WITH_OR_WITHOUT_MODIFIERS(self, node, visited_children):
    return visited_children[0]


def visit_GISMU(self, node, visited_children):
    literal = visited_children[0][0].text
    gismu_struct = self.dictionary.get_word_struct(literal)
    gismu_struct['sumti'] = self.dictionary.get_definition_arguments(literal)['args']
    return {literal: gismu_struct}
