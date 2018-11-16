from stanfordcorenlp import StanfordCoreNLP

from src.Refactoring.translate_questions import translate_questions
from src.Refactoring.syntax_check_questions import syntax_check_questions


def refactor_questions(nlp: StanfordCoreNLP, questions, translation: bool, debug):
    """

    :param nlp: StanfordCoreNLP instance
    :param questions: questions to refactor
    :param translation: Turn translation on or off
    :param debug: Debug on or off
    :return: Two arrays, correct_questions and garbage_questions
    """
    correct_questions, garbage_questions = syntax_check_questions(nlp, questions, debug)

    if translation:
        correct_questions = translate_questions(correct_questions, debug)

    return correct_questions, garbage_questions

