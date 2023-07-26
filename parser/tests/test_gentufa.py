import pytest

from parser.gentufa import Gentufa
from parsimonious.exceptions import IncompleteParseError

parser = Gentufa()


def test_chapter_sentences(request, build_test_parameters):
    chapter_number, line_number, sentence = build_test_parameters
    try:
        parser.get_parsed_sentence(sentence)
        print(f"Passed: Sentence '{sentence}' (Chapter {chapter_number} - Line {line_number})")
    except IncompleteParseError as e:
        pytest.fail(
            f"Sentence '{sentence}' (Chapter {chapter_number} - Line {line_number})"
        )
