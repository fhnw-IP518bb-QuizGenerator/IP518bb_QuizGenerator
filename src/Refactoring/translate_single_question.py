from textblob import TextBlob


def translate_single_question(question):
    """
    This function translates a question from german to english and back.

    :param question: Question to tranlate
    :return:
    """
    blob = TextBlob(question)
    en_question = blob.translate(from_lang='de',to='en')
    translated_question = en_question.translate(from_lang='en', to='de')

    return str(translated_question)
