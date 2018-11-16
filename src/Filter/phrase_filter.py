def phrase_filter(tree):
    """
    Filters for all noun phrases
    """
    return tree.label() in ['NP', 'MPN', 'PP', 'CNP', 'CVP', 'AP']