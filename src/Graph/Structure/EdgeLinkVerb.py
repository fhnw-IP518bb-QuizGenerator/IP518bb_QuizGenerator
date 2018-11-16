class EdgeLinkVerb:
    """
    A link bewteen two nodes: a verb
    """

    verb = ""
    tense = None

    def __init__(self, verb, tense):
        """
        Constructor
        :param verb:
        :param genus:
        :param tense:
        """
        self.verb = verb
        self.tense = tense

    def __str__(self):
        """
        String representation
        :return:
        """
        return self.verb + " " + str(self.tense)