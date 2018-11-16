from pprint import pprint
from src.Question.generate_single_question import generate_single_question

def generate_questions(edge, nlp, debug):
    """
    Generates questions from a given Node
    :param edge:
    :param nlp:
    :param debug:
    :return:
    """

    if debug:
        pprint(str(edge))

    return [generate_single_question(edge.node_1, edge.link, edge.node_2, nlp, debug), generate_single_question(edge.node_2, edge.link, edge.node_1, nlp, debug)]
