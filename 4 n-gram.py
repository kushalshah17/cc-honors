# prompt: load text.txt and do ngram in it

with open("text.txt", "r") as f:
  text = f.read()

from nltk import ngrams
n = 2
ngrams = ngrams(text.split(), n)
for gram in ngrams:
  print(gram)






# Let's create some sample text for demonstration
text = """N-gram can be defined as the contiguous sequence of n items from a given sample of text or speech."""

from nltk import ngrams

# Define the value of n for the n-grams
n = 2

# Split the text into words and generate n-grams
words = text.split()
ngrams_output = ngrams(words, n)

# Print the generated n-grams
for gram in ngrams_output:
    print(gram)