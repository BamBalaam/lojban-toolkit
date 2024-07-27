__all__ = ["visit_BRIVLA_WITH_CU", "visit_NAMED_ENTITY", "visit_PRONOUNS"]


def visit_PRONOUNS(self, node, visited_children):
    pronouns_definition = {
        "mi": "I/me, we/us",
        "do": "You",
        "ti": "This, these",
        "ta": "That, those",
        "tu": "That far away, those far away",
        "zo'e": "Unspecified value",
    }
    literal = visited_children[0][0].text
    return {
        literal: {"definition": pronouns_definition[literal], "type": "cmavo (pronoun)"}
    }


def visit_NAMED_ENTITY(self, node, visited_children):
    node_text = node.text.strip()
    return {node_text: {"type": "named entity"}}


def visit_BRIVLA_WITH_CU(self, node, visited_children):
    node_text = node.text.strip()
    return {
        node_text: {
            "type": "brivla with cu separator",
            "segments": [
                {"cu": {"definition": "selbri separator", "type": "cmavo"}},
                visited_children[2][0],
            ],
        }
    }
