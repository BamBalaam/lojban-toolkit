import sys
sys.path.append(".")

from inspect import getmembers, isfunction

from . import base_grammar, selmaho

functions = []

base_grammar_functions = getmembers(base_grammar, isfunction)
selmaho_functions = getmembers(selmaho, isfunction)

for function in base_grammar_functions:
    functions.append(function[1])
for function in selmaho_functions:
    functions.append(function[1])
