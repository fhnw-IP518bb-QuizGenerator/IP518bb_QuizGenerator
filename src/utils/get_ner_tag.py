def get_ner_tag(node, ner_tagging):
    """
    Returns the NER tag for a given node
    :param node:
    :param ner_tagging:
    :return:
    """
    return ner_tagging[node[2] - 1][1]