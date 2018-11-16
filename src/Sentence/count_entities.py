import re

def count_entities(sentence):
    """
    Counts the number of entities (A$, B$ etc.) in a sentence
    :param sentence:
    :return:
    """
    return len(re.findall("[A-Z+]\$", sentence))