from pprint import pprint
from stanfordcorenlp import StanfordCoreNLP
from src.Sentence.Sentence import Sentence
from json import JSONDecodeError


def simplify_sentence(nlp: StanfordCoreNLP, sentence_string, debug):
    """
    Simplifies a given sentence
    :param nlp:
    :param sentence_string:
    :param debug:
    :return:
    """

    if debug:
        print("-------------------------------------------------------------------------")
        pprint(sentence_string)

    # Create Sentence instance
    sentence = Sentence(sentence_string, nlp, [])

    try:
        split_sentences = sentence.replace_entities(debug).remove_inserted_sentences(debug).split_sentence(debug)
    except JSONDecodeError:
        return []

    return [sentence.sentence for sentence in split_sentences]