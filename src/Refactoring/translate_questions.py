from pprint import pprint
from src.Refactoring.translate_single_question import translate_single_question


def translate_questions(questions, debug):
    """
    Translates a set of questions
    """
    tranlated_questions = []
    for question in questions:
        tranlsation = translate_single_question(question)
        tranlated_questions.append(tranlsation)
        if debug:
            print("-------------------------------------------------------------------------")
            pprint(question + ' | ' + tranlsation)

    return tranlated_questions