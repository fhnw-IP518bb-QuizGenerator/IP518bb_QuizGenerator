from pprint import pprint

from  src.utils.is_verb import is_verb
from stanfordcorenlp import StanfordCoreNLP


def syntax_single_question(nlp: StanfordCoreNLP, question, debug):
    """
    Checks the syntax of a question to match general german grammar rules
    """
    pos_tagging = nlp.pos_tag(question)

    # checking if the second word of the question is a word.
    if is_verb(pos_tagging[1][1]):
        return True
    else:
        if debug:
            pprint("Throw away question: " + question)
        return False
