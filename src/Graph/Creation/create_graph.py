from pprint import pprint

import nltk
from stanfordcorenlp import StanfordCoreNLP
from pattern.de import SG, PL, gender, pluralize, tenses
from src.Graph.Structure.EdgeLinkVerb import EdgeLinkVerb
from src.Graph.Structure.Graph import Graph
from src.Graph.Structure.Node import Node
from src.Graph.Structure.Edge import Edge
from src.Filter.eos_filter import eos_filter
from src.Filter.noun_filter import noun_filter
from src.Filter.phrase_filter import phrase_filter


def create_graph(nlp: StanfordCoreNLP, sentence, debug = False):
    """
    Create a graph from a given sentence with a given StanfordCoreNLP instance
    :param nlp: StanfordCoreNLP instance
    :param sentence: Sentence to create a graph from
    :param debug: Debug mode
    :return:
    """

    if debug:
        print("-------------------------------------------------------------------------")
        pprint(sentence)

    # -------------------------------------------------------------------------
    # Create NLTK parse tree of entire sentence
    parsed_output = nlp.parse(sentence)
    parse_tree = nltk.tree.Tree.fromstring(parsed_output)

    if debug:
        print("------------")
        print("Entire tree:")
        parse_tree.pretty_print()

    # -------------------------------------------------------------------------
    # Get all noun phrases - those are possible Node candidates
    noun_phrases = list(parse_tree.subtrees(phrase_filter))

    # There's no noun phrases, this sentence is a little _to_ simple.
    if len(noun_phrases) == 0:
        noun_phrases = list(parse_tree.subtrees(noun_filter))

    if debug:
        print("------------")
        print("All noun phrase trees:")
        for noun_phrase in noun_phrases:
            noun_phrase.pretty_print()

    # -------------------------------------------------------------------------
    # Cleanups: Remove those that are nested in another nounphrase, we're interested in the bigger one
    for current_noun_phrase in noun_phrases:
        sub_noun_phrases = list(current_noun_phrase.subtrees(phrase_filter))
        if len(sub_noun_phrases) == 0:
            pass # There's no sub-noun-phrases, we can skip this

        # Iterate over sub noun phrases and remove all of them
        for sub_noun_phrase in sub_noun_phrases:
            if sub_noun_phrase == current_noun_phrase:
                continue # Don't remove yourself

            i = 0
            while i <= len(noun_phrases) - 1:
                if sub_noun_phrase == noun_phrases[i]:
                    del noun_phrases[i]
                i += 1

    if debug:
        print("------------")
        print("All noun phrase trees after cleanup:")
        for noun_phrase in noun_phrases:
            noun_phrase.pretty_print()

    # -------------------------------------------------------------------------
    # Remove those sub trees from the parse tree, left over can be considered links between those Nodes
    removable_tree = parse_tree[0]
    if removable_tree.label() != 'S':
        removable_tree = removable_tree[0]

    for noun_phrase in noun_phrases:
        try:
            removable_tree.remove(noun_phrase)
        except ValueError:
            pass # Trying to remove a sub-tree that isn't there anymore - skip it

    if len(noun_phrases) == 1: # There was only one nounphrase, so the other one is likely just a noun
        nouns = list(parse_tree.subtrees(noun_filter))
        if len(nouns) == 1: # Gotcha, that single noun is the other node candidate
            noun_phrases.append(nouns[0])
            try:
                removable_tree.remove(nouns[0])
            except ValueError:
                pass # In list, but not really, swallow

    # Remove end of sentence (i.e. $.), so it doesn't interfere with the rest
    eos_subtrees = list(parse_tree.subtrees(eos_filter))
    if len(eos_subtrees) > 0:
        try:
            removable_tree.remove(eos_subtrees[0])
        except ValueError:
            pass # Seems to be in list, but not really, swallow this error.

    if debug:
        print("------------")
        print("Rest of the tree after removing all noun-phrases:")
        parse_tree.pretty_print()

    # -------------------------------------------------------------------------
    # Create nodes and edge links

    nodes = []
    edge_links = []
    edges = []

    # Try to figure out what kind of NE the possible nodes are
    ner_tagging = nlp.ner(sentence)

    if debug:
        print("------------")
        print("NER tagging for entire sentence:")
        pprint(ner_tagging)

    # Create nodes
    for noun_phrase in noun_phrases:
        # Create the word itself
        leaves = noun_phrase.leaves()
        node_word = " ".join(leaves)
        node_ne_tag = "O"
        node_numerus = SG

        # Try to find the corresponding NER
        for current_tag in ner_tagging:
            if current_tag[1] != 'O' and current_tag[0] in leaves:
                node_ne_tag = current_tag[1]

        # Grab the first noun of the sentence
        nouns = list(noun_phrase.subtrees(noun_filter))
        if len(nouns) == 0:
            # No nouns in this phrase, no nodes created.
            continue
        noun = " ".join(nouns[0].leaves())

        # Try to determine the gender
        node_gender = gender(noun)

        # Try to determine the numerus
        if pluralize(noun) == noun and node_ne_tag == 'O':
            node_numerus = PL

        nodes.append(Node(node_word, node_ne_tag, node_gender, node_numerus))

    if debug:
        print("------------")
        print("Nodes created:")
        for node in nodes:
            pprint(str(node))

    # Create edge links
    edge_leaves = parse_tree.leaves()
    for edge_leave in edge_leaves:
        link_word = edge_leave
        link_tense = None

        try:
            link_tenses = tenses(link_word)
            if len(link_tenses) > 0:
                link_tense = link_tenses[0] # Take first, this one is most likely
        except ValueError:
            pass # Something in the intestines of pattern.de went wrong, swallow

        edge_links.append(EdgeLinkVerb(link_word, link_tense))

    if debug:
        print("------------")
        print("Edge links created:")
        for edge_link in edge_links:
            pprint(str(edge_link))

    # -------------------------------------------------------------------------
    # Stick nodes and edge links together: they form the graph

    # The edges are, within the sentence, between two nodes in the pattern of "Node - Edge - Node"
    # Therefore, the first node, together with the second node and the first link forms one graph

    i = 0
    while i <= len(nodes) - 2 and i <= len(edge_links) - 1:
        first_node = nodes[i]
        second_node = nodes[i + 1]

        edge = Edge(first_node, edge_links[i], second_node)

        first_node.attach_edge(edge)
        second_node.attach_edge(edge)

        edges.append(edge)

        i += 1

    if debug:
        for edge in edges:
            print("------------")
            print("Edges created:")
            pprint(str(edge))

    # -------------------------------------------------------------------------
    # Create graph collection
    return Graph(nodes, edges)