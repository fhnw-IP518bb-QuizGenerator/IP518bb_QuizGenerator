from src.utils.is_noun import is_noun

def should_be_small(pos_tag):
    """
    Determiens if a word should be written small, depending on its POS tag
    :param pos_tag:
    :return:
    """

    return is_noun(pos_tag)