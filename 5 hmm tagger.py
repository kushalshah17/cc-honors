import nltk
import numpy as np
import pandas as pd

class HMMTagger:
    def __init__(self):
        self.tags = set()
        self.words = set()
        self.transition_probs = {}
        self.emission_probs = {}

    def train(self, corpus):
        # Collecting tags and words
        for sentence in corpus:
            for word, tag in sentence:
                self.tags.add(tag)
                self.words.add(word)

        # Initializing count matrices
        tag_count = {tag: 0 for tag in self.tags}
        word_tag_count = {word: {tag: 0 for tag in self.tags} for word in self.words}
        tag_transition_count = {tag1: {tag2: 0 for tag2 in self.tags} for tag1 in self.tags}

        # Counting occurrences
        for sentence in corpus:
            previous_tag = None
            for word, tag in sentence:
                tag_count[tag] += 1
                word_tag_count[word][tag] += 1
                if previous_tag:
                    tag_transition_count[previous_tag][tag] += 1
                previous_tag = tag

        # Calculating probabilities
        self.transition_probs = {tag1: {tag2: tag_transition_count[tag1][tag2] / tag_count[tag1]
                                        for tag2 in self.tags}
                                 for tag1 in self.tags}

        self.emission_probs = {word: {tag: word_tag_count[word][tag] / tag_count[tag]
                                      for tag in self.tags}
                               for word in self.words}

        # Printing the corpus dataset
        print("Corpus Dataset:")
        for sentence in corpus:
            print(sentence)
        print()

        # Printing emission probability matrix
        print("Emission Probability Matrix:")
        print(pd.DataFrame(self.emission_probs).fillna(0))
        print()

        # Printing state transition probability matrix
        print("State Transition Probability Matrix:")
        print(pd.DataFrame(self.transition_probs).fillna(0))
        print()

    def predict(self, sentence):
        predicted_tags = []
        previous_tag = None

        for word in sentence:
            max_prob = 0
            best_tag = None
            for tag in self.tags:
                # Calculate emission probability
                emission_prob = self.emission_probs.get(word, {}).get(tag, 0)
                # Calculate transition probability
                transition_prob = self.transition_probs.get(previous_tag, {}).get(tag, 0) if previous_tag else 1
                # Calculate total probability
                prob = emission_prob * transition_prob

                if prob > max_prob:
                    max_prob = prob
                    best_tag = tag
            predicted_tags.append(best_tag)
            previous_tag = best_tag

        return predicted_tags

# Example training corpus
training_corpus = [
    [("I", "PRON"), ("like", "VERB"), ("cats", "NOUN")],
    [("He", "PRON"), ("likes", "VERB"), ("dogs", "NOUN")],
    [("She", "PRON"), ("likes", "VERB"), ("cats", "NOUN")],
]

# Test sentence
test_sentence = ["She", "likes", "dogs"]

# Create and train HMM
hmm = HMMTagger()
hmm.train(training_corpus)

# Predict tags for test sentence
predicted_tags = hmm.predict(test_sentence)
print("Predicted tags:", predicted_tags)
