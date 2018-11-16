class Graph:
    """
    Collection of nodes and edges
    """

    nodes = []
    edges = []

    def __init__(self, nodes, edges):
        """
        Constructor
        :param nodes:
        :param edges:
        """
        self.nodes = nodes
        self.edges = edges