import pytest

from grammar_parser import Gentufa
from visitor import GentufaVisitor
from parsimonious.exceptions import IncompleteParseError, ParseError, VisitationError

parser = Gentufa()


def test_chapter_sentences(build_test_parameters):
    chapter_number, line_number, sentence = build_test_parameters
    try:
        parse_tree = parser.get_parsed_text(sentence)
    except (IncompleteParseError, ParseError):
        pytest.fail(
            f"Parser fail - Sentence '{sentence}' (Chapter {chapter_number} - Line {line_number})"
        )
    try:
        visted_tree = GentufaVisitor(parse_tree)
        visted_tree.get_json_output()
    except (VisitationError, TypeError):
        pytest.fail(
            f"Visitor fail - Sentence '{sentence}' (Chapter {chapter_number} - Line {line_number})"
        )
