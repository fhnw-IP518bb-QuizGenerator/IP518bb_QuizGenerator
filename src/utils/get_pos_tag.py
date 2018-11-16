def get_pos_tag(node, pos_tagging):
    """
    Returns the POS tag for a given node
    :param node:
    :param tokens:
    :param pos_tagging:
    :return:
    """
    return pos_tagging[node[2] - 1][1]