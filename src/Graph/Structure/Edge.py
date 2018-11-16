import sys
sys.path.append('./../../../')

from src.Graph.Structure.Node import Node
from src.Graph.Structure.EdgeLinkVerb import EdgeLinkVerb

class Edge:
    """
    An edge between two nodes
    """

    node_1 = None
    link = None
    node_2 = None

    def __init__(self, node_1: Node, link: EdgeLinkVerb, node_2: Node):
        """
        Constructor
        :param node_1:
        :param link:
        :param node_2:
        """
        self.node_1 = node_1
        self.link = link
        self.node_2 = node_2

    def __str__(self):
        """
        String representation
        :return: str
        """
        return "[" + str(self.node_1) + "] --(" + str(self.link) + ")--> [" + str(self.node_2) + "]"

    def get_other_node(self, this_node):
        """
        Returns the other node that is not this_node
        :param this_node:
        :return:
        """
        if self.node_1 == this_node:
            return self.node_2

        return self.node_1