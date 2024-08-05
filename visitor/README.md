# GentufaVisitor

This Python module goes through a parsed lojban sentence and generates a JSON representation with all its elements tagged and defined.

## Usage

Module can either be imported and used in other python files

```
from grammar_parser import Gentufa
from visitor import GentufaVisitor

parse_tree = Gentufa().get_parsed_text("mi klama le zarci")
visitor = GentufaVisitor(parse_tree)
visitor.get_json_output()
```

or run as-is

`python3 visitor/gentufa_visitor.py "mi klama le zarci"`