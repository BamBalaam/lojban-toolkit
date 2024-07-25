import json

from visitor.visitor import GentufaVisitor

sentence = "la meris cu melbi se tavla la tam"
output = GentufaVisitor(sentence).get_output()
print(json.dumps(output))