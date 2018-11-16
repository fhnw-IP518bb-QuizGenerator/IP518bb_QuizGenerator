def accuracy(refactored_questions, garbage_questions):
    """
    Calculates and prints percentage of questions that are garbage/good
    :param refactored_questions:
    :param garbage_questions:
    :return:
    """

    no_refactored = len(refactored_questions)
    no_garbage = len(garbage_questions)
    total = no_refactored + no_garbage

    percentage_good = 100 * no_refactored / total
    percentage_garbage = 100 * no_garbage / total

    print("++++++++++++++++++++++++++++++")
    print("+  Total number of questions: " + str(total))
    print("+     number of good-enough questions: " + str(no_refactored))
    print("+     number of garbage questions: " + str(no_garbage))
    print("++++++++++++++++++++++++++++++")
    print("+  Percentage of good-enough questions: " + str(percentage_good))
    print("+  Percentage of garbage questions: " + str(percentage_garbage))
    print("++++++++++++++++++++++++++++++")