from pprint import pprint
from src.utils.should_be_small import should_be_small

def cleanup(question, nlp, debug):
    """
    Cleans a question sentence of things like ` , ` (spaces around comma) etc.
    :param question:
    :param nlp:
    :param nltk:
    :return:
    """

    words = []

    pos_tagging = nlp.pos_tag(question)


    if debug:
        pprint(pos_tagging)

    for pos_tag in pos_tagging:
        if should_be_small(pos_tag[1]):
            words.append(pos_tag[0])
        else:
            words.append(pos_tag[0].lower())

    question = " ".join(words)

    question = question.replace(" , ", ", ")
    question = question.replace(" ?", "?")
    question = question[0].upper() + question[1:len(question)]

    return question
