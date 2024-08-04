from parsimonious.nodes import Node

def visit_LOJBAN_TEXT(self, node, visited_children):
    for child in visited_children[:-1]:
        if type(child) is not Node:
            self.output["sentences"].append(child)
    return

def visit_SENTENCE(self, node, visited_children):
    sentence = {"sentence": node.text, "segments": []}
    for child in visited_children:
        sentence["segments"].append(child)
    return sentence

def visit_SUBSEQUENT_SENTENCE(self, node, visited_children):
    return visited_children[1]

def visit_LOJBAN_WORDS_OR_EXPRESSIONS(self, node, visited_children):
    return visited_children[0]

def visit_CMAVO(self, node, visited_children):
    return visited_children[0]

def visit_TANRU_OR_BRIVLA(self, node, visited_children):
    return visited_children[0]

def visit_BRIVLA(self, node, visited_children):
    return visited_children[0]

def visit_TANRU(self, node, visited_children):
    return visited_children

def visit_GISMU(self, node, visited_children):
    literal = visited_children[0][0].text
    gismu_struct = self.dictionary.get_word_struct(literal)
    gismu_struct["sumti"] = self.dictionary.get_definition_arguments(literal)["args"]
    return {literal: gismu_struct}

def visit_LUJVO(self, node, visited_children):
    literal = visited_children[0][0].text
    lujvo_struct = self.dictionary.get_word_struct(literal)
    lujvo_struct["sumti"] = self.dictionary.get_definition_arguments(literal)["args"]
    return {literal: lujvo_struct}

def visit_FUhIVLA(self, node, visited_children):
    literal = visited_children[0][0].text
    fuhivla_struct = self.dictionary.get_word_struct(literal)
    fuhivla_struct["sumti"] = self.dictionary.get_definition_arguments(literal)["args"]
    return {literal: fuhivla_struct}

def visit_CMENE(self, node, visited_children):
    literal = visited_children[0][0].text
    return {literal: {"type": "cmene", "definition": "name of a person or thing"}}
