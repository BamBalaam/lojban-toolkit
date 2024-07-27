from . import base_grammar, chapter2

base_grammar_functions = []
chapter2_functions = []
for function_name in base_grammar.__all__:
    base_grammar_functions.append(getattr(base_grammar, function_name))
for function_name in chapter2.__all__:
    chapter2_functions.append(getattr(chapter2, function_name))

functions = tuple(base_grammar_functions) + tuple(chapter2_functions)
