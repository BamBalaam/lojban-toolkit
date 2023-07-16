from parser.gentufa import Gentufa
from visitor.visitor import GentufaVisitor

from pprint import pprint

parser = Gentufa()
#tree = parser.get_parsed_sentence("ci pi pa vo pa mu")

output = GentufaVisitor("tavla do ti")
#output = visitor.visit(tree)
print(output.sentence)
