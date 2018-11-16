from src.Refactoring.cleanup import cleanup


def generate_single_question(answer_node, edge_link, info_node, nlp, debug):
    """
    Generates a single question for a given set of nodes
    :param answer_node:
    :param edge_link:
    :param info_node:
    :param nlp:
    :param debug:
    :return:
    """

    try:
        # verb = conjugate(edge_link.verb, edge_link.tense[0], edge_link.tense[1], answer_node.numerus)
        verb = edge_link.verb
    except TypeError:
        if debug:
            print("No verb, skipping...")
        return ""

    if verb == None:
        if debug:
            print("Was not able to conjugate verb: " + edge_link.verb)
        return ""

    question = answer_node.get_question_word() + " " + verb + " " + info_node.word + "?"
    question = cleanup(question, nlp, debug)

    return question
