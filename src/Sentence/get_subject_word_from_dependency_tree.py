from pprint import pprint

def get_subject_word_from_dependency_tree(tree, tokens):
    """
    Returns the word which can be considered the subject of a sentence
    :param tree:
    :param tokens:
    :return:
    """

    # Find root node
    root = None
    for node in tree:
        if node[0] == 'ROOT':
            root = node
            break

    # Find first attached nsubj
    for node in tree:
        if (node[0] == 'nsubj' or node[0] == 'name') and node[1] == root[2]:
            return tokens[node[2] - 1]

    return None