def noun_filter(tree):
    """
    Filter for all nouns
    """
    return tree.label() in ['NE', 'NN', 'PPER']