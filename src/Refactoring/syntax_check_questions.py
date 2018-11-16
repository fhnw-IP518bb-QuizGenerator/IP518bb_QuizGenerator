
from stanfordcorenlp import StanfordCoreNLP

from src.Refactoring.syntax_single_question import syntax_single_question


def syntax_check_questions(nlp: StanfordCoreNLP, questions, debug):
    """

    :param nlp: StanfordCoreNLP instance
    :param questions: questions to check
    :param debug: Debug on or off
    :return: correct questions and incorrect questions
    """
    syntax_correct = []
    syntax_uncorrect = []
    for question in questions:
        if syntax_single_question(nlp, question, debug):
            syntax_correct.append(question)
        else:
            syntax_uncorrect.append(question)

    return syntax_correct, syntax_uncorrect
