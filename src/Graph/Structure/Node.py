class Node:
    """
    A single node, i.e. an entity that can be asked for
    :return:
    """

    word = ""
    ne_type = ""
    gender = ""
    numerus = ""
    attached_edges = []

    def __init__(self, word, ne_type, gender, numerus):
        """
        Constructor
        :param word:
        :param ne_type:
        :param gender:
        :param numerus:
        """
        self.word = word
        self.ne_type = ne_type
        self.gender = gender
        self.numerus = numerus
        self.attached_edges = []

    def __str__(self):
        """
        String representation
        :return:
        """
        return self.word + " (" + str(self.ne_type) + " / " + str(self.gender) + " / " + str(self.numerus) + ")"

    def attach_edge(self, edge):
        """
        Add a newly attached edge
        :param edge: Newly attached edge
        :return: None
        """
        self.attached_edges.append(edge)

    def get_attached_edges(self, coming_from_edge):
        """
        Get all attached edges except the one we're actually coming from
        :param coming_from_edge:
        :return:
        """
        attached_edges = []
        for attached_edge in self.attached_edges:
            if attached_edge != coming_from_edge:
                attached_edges.append(attached_edge)

        return attached_edges

    def get_question_word(self):
        """
        Determines the question word
        :return:
        """
        switcher = {
            'O': 'Was',
            'YEAR': 'Wann',
            'PERSON': 'Wer',
            'LOCATION': 'Wo',
            'ORGANIZATION': 'Wer',
            'CITY': 'Was',
            'CARD': 'Wie viele',
            'MISC': 'Was',
        }

        return switcher.get(self.ne_type, 'Invalid named entity type: ' + self.ne_type)

