def visit_BO(self, node, visited_children):
    literal = visited_children[0][0].text
    return {literal: {"definition": "scope grouping", "type": "cmavo / selma'o BO"}}

def visit_SELMAhO_SE(self, node, visited_children):
    definition = {
        "se": "Swap x1 and x2 in the following selbri",
        "te": "Swap x1 and x3 in the following selbri",
        "ve": "Swap x1 and x4 in the following selbri",
        "xe": "Swap x1 and x5 in the following selbri",
    }
    literal = visited_children[0][0].text
    return {
        literal: {
            "definition": definition[literal],
            "type": "cmavo / selma'o SE / varying order of sumti",
        }
    }

def visit_SELMAhO_LE(self, node, visited_children):
    definition = {
        "le": "The, the one(s) described as",
        "lo": "Some, some of those which really are",
    }
    literal = visited_children[0][0].text
    return {
        literal: {
            "definition": definition[literal],
            "type": "cmavo / selma'o LE / description",
        }
    }

def visit_KU(self, node, visited_children):
    return {
        "ku": {
            "definition": "elidable terminator",
            "type": "cmavo / selma'o KU",
        }
    }

def visit_SELMAhO_LAhE(self, node, visited_children):
    definition = {
        "la'e": "Something referred to by",
        "lu'e": "A reference to",
        "tu'a": "An abstraction involving",
        "lu'a": "An individual/member/component of",
        "lu'i": "A set formed form",
        "lu'o": "A mass formed from",
        "vu'i": "A sequence formed from",
    }
    literal = visited_children[0][0].text
    return {
        literal: {
            "definition": definition[literal],
            "type": "cmavo / selma'o LAhE / sumti qualifier",
        }
    }

def visit_LUhU(self, node, visited_children):
    return {
        "lu'u": {
            "definition": "elidable terminator",
            "type": "cmavo / selma'o LUhU",
        }
    }

def visit_COI(self, node, visited_children):
    return {
        "coi": {
            "definition": "greeting",
            "type": "cmavo / selma'o COI",
        }
    }

def visit_LA(self, node, visited_children):
    return {
        "la": {
            "definition": "the ones named",
            "type": "cmavo / selma'o LA / named entity",
        }
    }

def visit_SELMAhO_KOhA(self, node, visited_children):
    return visited_children[0]

def visit_KOhA_MI_SERIES(self, node, visited_children):
    pronouns_definition = {
        "mi": "I/me",
        "mi'o": "You and I",
        "mi'a": "I and others, we but not you",
        "ma'a": "You and I and others",
        "do": "You",
        "do'o": "You and others",
        "ko": "You - imperative",
    }
    literal = visited_children[0][0].text
    return {
        literal: {
            "definition": pronouns_definition[literal],
            "type": "cmavo / selma'o KOhA (mi series) / personal pronouns",
        }
    }

def visit_KOhA_TI_SERIES(self, node, visited_children):
    pronouns_definition = {
        "ti": "This, these",
        "ta": "That, those",
        "tu": "That far away, those far away",
    }
    literal = visited_children[0][0].text
    return {
        literal: {
            "definition": pronouns_definition[literal],
            "type": "cmavo / selma'o KOhA (ti series) / demonstrative pronouns",
        }
    }

def visit_KOhA_DIhU_SERIES(self, node, visited_children):
    pronouns_definition = {
        "di'u": "The previous utterance",
        "de'u": "An earlier utterance",
        "da'u": "A much earlier utterance",
        "di'e": "The next utterance",
        "de'e": "A later utterance",
        "da'e": "A much later utterance",
        "dei": "This very utterance",
        "do'i": "Some utterance",
    }
    literal = visited_children[0][0].text
    return {
        literal: {
            "definition": pronouns_definition[literal],
            "type": "cmavo / selma'o KOhA (di'u series) / utterance pronouns",
        }
    }

def visit_KOhA_RI_SERIES(self, node, visited_children):
    pronouns_definition = {
        "ri": "Repeats last sumti",
        "ra": "Repeats previous sumti",
        "ru": "Repeats long-ago sumti",
    }
    literal = visited_children[0][0].text
    return {
        literal: {
            "definition": pronouns_definition[literal],
            "type": "cmavo / selma'o KOhA (ri series) / anaphoric pronouns",
        }
    }

def visit_KOhA_ZOhE_SERIES(self, node, visited_children):
    pronouns_definition = {
        "zo'e": "Obvious value",
        "zu'i": "Typical value",
        "zi'o": "Nonexistent value",
    }
    literal = visited_children[0][0].text
    return {
        literal: {
            "definition": pronouns_definition[literal],
            "type": "cmavo / selma'o KOhA (zo'e series) / indefinite pronouns",
        }
    }

def visit_KOhA_OTHER(self, node, visited_children):
    return visited_children[0]

def visit_MA(self, node, visited_childre):
    return {
        "ma": {
            "definition": "asking a sumti question",
            "type": "cmavo / selma'o KOhA",
        }
    }

def visit_SELMAhO_GOhA(self, node, visited_children):
    return visited_children[0]

def visit_GOhA_GOhI_SERIES(self, node, visited_children):
    pronouns_definition = {
        "go'i": "Repeats last bridi",
        "go'a": "Repeats previous bridi",
        "go'u": "Repeats long-ago bridi",
        "go'e": "Repeats last-but-one bridi",
        "go'o": "Repeats future bridi",
        "nei" : "Repeats current bridi",
        "no'a": "Repeats outer bridi",
    }
    literal = visited_children[0][0].text
    return {
        literal: {
            "definition": pronouns_definition[literal],
            "type": "cmavo / selma'o GOhA (go'i series) / anaphoric pronouns",
        }
    }

def visit_GOhA_OTHER(self, node, visited_children):
    return visited_children[0]

def visit_MO(self, node, visited_children):
    return {
        "mo": {
            "definition": "asking a bridi question",
            "type": "cmavo / selma'o GOhA",
        }
    }

def visit_CU(self, node, visited_children):
    return {
        "cu": {
            "definition": "separator",
            "type": "cmavo / selma'o CU",
        }
    }

def visit_SELMAhO_VA(self, node, visited_children):
    definition = {
        "vi": "short distance",
        "va": "medium distance",
        "vu": "long distance",
    }
    literal = visited_children[0][0].text
    return {
        literal: {
            "definition": definition[literal],
            "type": "cmavo / selma'o VA / spacial tense",
        }
    }

def visit_SELMAhO_FAhA(self, node, visited_children):
    definition = {
        "zu'a": "left",
        "ri'u": "right",
        "ga'u": "up",
        "ni'a": "down",
        "ca'u": "front",
        "ne'i": "within",
    }
    literal = visited_children[0][0].text
    return {
        literal: {
            "definition": definition[literal],
            "type": "cmavo / selma'o FAhA / spacial tense",
        }
    }

def visit_SELMAhO_PU(self, node, visited_children):
    definition = {
        "pu": "past",
        "ca": "present",
        "ba": "future",
    }
    literal = visited_children[0][0].text
    return {
        literal: {
            "definition": definition[literal],
            "type": "cmavo / selma'o PU / temporal tense",
        }
    }

def visit_SELMAhO_ZI(self, node, visited_children):
    definition = {
        "zi": "short time distance",
        "za": "medium time distance",
        "zu": "long time distance",
    }
    literal = visited_children[0][0].text
    return {
        literal: {
            "definition": definition[literal],
            "type": "cmavo / selma'o ZI / temporal tense",
        }
    }
