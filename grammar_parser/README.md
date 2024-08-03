# Gentufa

This Python module allows the user to parse a lojban sentence, assert if it is valid, and get its Parse Tree.

## Usage

Module can either be imported and used in other python files

```
from grammar_parser import Gentufa

parser = Gentufa()
parsed_sentence = parser.get_parsed_sentence("mi klama le zarci")
```

or run as-is

`python3 grammar_parser/gentufa.py "mi klama le zarci"`