from parser.gentufa import Gentufa
from visitor.visualise import GentufaVisualisor

from pprint import pprint

parser = Gentufa()
#tree = parser.get_parsed_sentence("ci pi pa vo pa mu")

test = parser.get_parsed_sentence("mi tavla do le tavla ku")

print(test)

import pdb; pdb.set_trace()

output = GentufaVisualisor("mi tavla do le tavla ku")
#output = visitor.visit(tree)
#print(output.sentence)
