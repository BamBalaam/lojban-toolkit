import os

import pytest


def sentences():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )

    # Get all files with the Lojban sentences to test the parser against
    chapter_files = os.listdir(os.path.join(__location__, "sentences"))

    # WIP
    #chapter_files = ["chapter_2.txt"]

    sentences = []
    for chap_file in chapter_files:
        file_path = os.path.join(__location__, f"sentences/{chap_file}")
        # Filename to chapter name (e.g. chapter_2.txt -> Chapter 2)
        chapter_name = chap_file.replace(".txt", "").replace("_", " ")
        # Extract chapter number
        chapter_number = chapter_name.split(" ")[1]
        # Get sentences from file
        with open(file_path, "r") as f:
            line_number = 1
            for sentence in f.readlines():
                # Ignore comments grouping sentences by subsection
                # and whitespaces
                if sentence[0] != "#" and sentence.strip() != '':
                    sentences.append((chapter_number, line_number, sentence.strip()))
                line_number += 1
    return sentences


@pytest.fixture(params=sentences())
def build_test_parameters(request):
    chapter_number, line_number, sentence = request.param
    yield chapter_number, line_number, sentence
