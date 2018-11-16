def is_noun(label):
    """
    Determines if the given POS label represents a noun
    :param label:
    :return:
    """
    return label in ['NE', 'NN']