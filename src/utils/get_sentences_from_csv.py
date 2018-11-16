import csv

def get_sentences_from_csv(file_path):
    """
    Loads all sentences from a given CSV file
    :param file_path:
    :return:
    """

    sentences = []

    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if len(row) == 1:
                sentences.append(row[0])

    return sentences