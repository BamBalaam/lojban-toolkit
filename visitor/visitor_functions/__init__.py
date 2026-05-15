from inspect import getmembers, isfunction

from . import base_grammar, selmaho

functions = [
    f[1]
    for f in getmembers(base_grammar, isfunction) + getmembers(selmaho, isfunction)
]
