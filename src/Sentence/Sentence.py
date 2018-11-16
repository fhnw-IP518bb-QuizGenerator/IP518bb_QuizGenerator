import re
import nltk
from pprint import pprint
from src.Filter.phrase_filter import phrase_filter
from src.Filter.noun_filter import noun_filter
from src.Sentence.get_subject_word_from_dependency_tree import get_subject_word_from_dependency_tree


class Sentence:
    """
    Represents a sentence
    """

    sentence = ""
    entities = []
    nlp = None

    def __init__(self, sentence, nlp, entities=[]):
        """
        Constructor
        :param sentence: The sentence as string
        :param nlp: StanfordCoreNLP instance
        """
        self.sentence = sentence
        self.entities = entities
        self.nlp = nlp

    def replace_entities(self, debug=False):
        """
        Replaces the noun phrases and such in the given sentence
        :param debug:
        :param nlp:
        :return:
        """
        parsed_output = self.nlp.parse(self.sentence)
        parse_tree = nltk.tree.Tree.fromstring(parsed_output)

        if debug:
            print("------------")
            print("Entire tree:")
            parse_tree.pretty_print()

        phrases = list(parse_tree.subtrees(phrase_filter))
        nouns = list(parse_tree.subtrees(noun_filter))

        node_tokens = phrases + nouns

        if debug:
            print("------------")
            print("All phrases:")
            for phrase in node_tokens:
                phrase.pretty_print()
                flattened = " ".join(phrase.leaves())
                if debug:
                    pprint("flattened: " + flattened)

        self.sentence = self.sentence.replace(',', ' ,')

        i = 97  # lower case A
        for phrase in node_tokens:
            key = chr(i).upper() + "$"
            value = " ".join(phrase.leaves())

            sentence_before = self.sentence
            self.sentence = self.sentence.replace(value, key)

            # If something actually got replaced
            if sentence_before != self.sentence:
                self.entities.append((key, value))

                if debug:
                    pprint("Removing '" + value + "' as " + key)

                i += 1

        return self

    def remove_inserted_sentences(self, debug=False):
        """
        Get rid of inserted sentences (i.e. everything between two commas, that was not part of an entity)
        :param debug:
        :return:
        """
        self.sentence = re.sub(',[^,]+,', '', self.sentence)
        self.sentence = re.sub('\([^\(\)]+\)', '', self.sentence)
        self.sentence = re.sub('\[[^\[\]]+\]', '', self.sentence)
        self.sentence = re.sub('\<[^\<\>]+\>', '', self.sentence)
        self.sentence = self.sentence.replace('  ', ' ')
        if debug:
            print("------------")
            print("Sentence without inserted sentences")
            pprint(self.sentence)

        return self

    def split_sentence(self, debug=False):
        """
        Splits this sentence: returns a list of smaller, simpler sentences
        :return:
        """
        sentence = self.sentence
        sentences = [Sentence(u.strip(), self.nlp, self.entities) for s in sentence.split(",") for t in s.split("und") for u in t.split("aber") if len(u.strip()) > 0]

        if debug:
            print("------------")
            print("Split sentences:")
            for sentence in sentences:
                pprint(sentence.sentence)

        # More than once split sentence, we need the subject in all of them
        if len(sentences) > 1:
            sentence_with_entities = self.readd_entities(debug)
            dependencies = self.nlp.dependency_parse(sentence_with_entities)

            if debug:
                print("------------")
                print("Dependency graph of simplified full sentence:")
                pprint(dependencies)

            # Get subject entity in order to attach it to any split sentence
            subject = get_subject_word_from_dependency_tree(dependencies, nltk.tokenize.word_tokenize(sentence_with_entities))

            if subject == None:
                if debug:
                    print("Error parsing sentence, subject was nout found in any entity. Swallowing all.")
                return []

            if debug:
                print("Subject of sentence:")
                pprint(subject)

            # Find subject entity
            subject_entity = None
            for entity in self.entities:
                if subject in entity[1]:
                    subject_entity = entity[0]
                    break

            if subject_entity == None:
                if debug:
                    print("Error parsing sentence, subject was nout found in any entity. Swallowing all.")
                return []

            if debug:
                print("Subject to be found in entity: " + subject_entity)

            # Add subject to any split sentence
            for sub_sentence in sentences:
                if subject_entity not in sub_sentence.sentence: # Not the sentence we've got the subject from
                    sub_sentence.sentence = subject_entity + " " + sub_sentence.sentence

        # Re-add all entities in order to have full sentences again
        for sentence in sentences:
            sentence.sentence = sentence.readd_entities(debug)

        return sentences

    def readd_entities(self, debug):
        """
        Re-adds entities to the sentence, thereby creating a copy of it
        :param debug:
        :return:
        """
        sentence = self.sentence

        if debug:
            print("------------")

        for entity in self.entities:
            if debug:
                print('Readding ' + entity[0])

            sentence = sentence.replace(entity[0], entity[1])

        if debug:
            print("Full sentence with entities:")
            pprint(sentence)

        return sentence
