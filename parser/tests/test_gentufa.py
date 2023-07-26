import os

import pytest

from parser.gentufa import Gentufa
from parsimonious.exceptions import IncompleteParseError

parser = Gentufa()


def sentences():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )

    # Get all files with the Lojban sentences to test the parser against
    chapter_files = os.listdir(os.path.join(__location__, "sentences"))

    # WIP
    chapter_files = ["chapter_2.txt"]

    sentences = []
    for chap_file in chapter_files:
        file_path = os.path.join(__location__, f"sentences/{chap_file}")
        # Filename to chapter name (e.g. chapter_2.txt -> Chapter 2)
        chapter_name = chap_file.replace(".txt", "").replace("_", " ")
        chapter_name = chapter_name.capitalize()
        # Get sentences from file
        with open(file_path, "r") as f:
            for sentence in f.readlines():
                # Ignore comments grouping sentences by subsection
                if sentence[0] != "#" or sentence.strip() == '':
                    print(sentence)
                    sentences.append((chapter_name, sentence.strip()))
    return sentences


@pytest.fixture(params=sentences())
def chapter_id_and_sentence(request):
    chapter_id, sentence = request.param
    yield chapter_id, sentence


def test_chapter_sentences(chapter_id_and_sentence):
    chapter_id, sentence = chapter_id_and_sentence
    try:
        parser.get_parsed_sentence(sentence)
    except IncompleteParseError as e:
        pytest.fail(
            f"Sentence '{sentence}' ({chapter_id})"
        )
