import json

from visitor import GentufaVisitor

sentence = "la meris cu melbi se tavla la tam"
output = GentufaVisitor(sentence).get_output()
print(json.dumps(output))