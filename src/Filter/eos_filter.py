def eos_filter(tree):
    """
    Filters for the end of sentencxe (i.e. period)
    """
    return tree.label() in ['$.']