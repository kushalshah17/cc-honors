import string
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Open the sample text file
with open("/content/ind.txt", "r") as f:
    # Read the lines from the file
    lines = f.readlines()

# Initialize the PorterStemmer object
ps = PorterStemmer()

# Loop through each line in the file
for line in lines:
    # Remove punctuation from the line
    line_no_punct = line.translate(str.maketrans("", "", string.punctuation))

    # Tokenize the line
    word_tokens = word_tokenize(line_no_punct)

    # Print the header
    print("{0:20}{1:20}".format("--Word--","--Stem--"))

    # Stem each word and print the results
    for word in word_tokens:
        print ("{0:20}{1:20}".format(word, ps.stem(word)))