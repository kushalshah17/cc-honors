#user input
!pip install nltk
!python -m nltk.downloader averaged_perceptron_tagger
import nltk
nltk.download('punkt')
from nltk import word_tokenize ,pos_tag, RegexpParser
from nltk.tag import pos_tag

sentence="It was a crazy weekend with college projects"

tokens= word_tokenize(sentence)

pos_tags=pos_tag(tokens)

chunks_patterns="NP:{<DT>?<JJ>*<NN>}"
chunks_parser= RegexpParser(chunks_patterns)
chunks= chunks_parser.parse(pos_tags)
print(chunks)






#input from document
import nltk
from nltk import word_tokenize ,pos_tag, RegexpParser
from nltk.tag import pos_tag
with open("/content/ind.txt", "r") as f:
    sentence = f.read()
tokens= word_tokenize(sentence)

pos_tags=pos_tag(tokens)

chunks_patterns="NP:{<DT>?<JJ>*<NN>}"
chunks_parser= RegexpParser(chunks_patterns)
chunks= chunks_parser.parse(pos_tags)
print(chunks)