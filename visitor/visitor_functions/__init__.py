import sys
sys.path.append(".")

from inspect import getmembers, isfunction

from . import base_grammar, selmaho

base_grammar_functions = getmembers(base_grammar, isfunction)
base_grammar_function_names = []
selmaho_functions = getmembers(selmaho, isfunction)
selmaho_function_names = []

for function in base_grammar_functions:
    base_grammar_function_names.append(function[1])
for function in selmaho_functions:
    selmaho_function_names.append(function[1])

functions = tuple(base_grammar_function_names) + tuple(selmaho_function_names)
