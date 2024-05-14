#input text by user
import spacy

nlp= spacy.load("en_core_web_sm")

text="It was a crazy weekend with college projects"
doc=nlp(text)
noun_chunks = list(doc.noun_chunks)
noun_chunks




#cognitive computing exp 1
#input text from document
import spacy
from builtins import open
import spacy
nlp = spacy.load("en_core_web_sm")
with open("/content/ind.txt", "r") as f:
    text = f.read()
doc = nlp(text)
noun_chunks = list(doc.noun_chunks)
noun_chunks