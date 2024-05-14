import nltk
nltk.download('punkt')
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
with open("/content/ind.txt", "r") as f:
    text = f.read()
print("Text:", text)
tokens = word_tokenize(text.lower())
print("Tokens:", tokens)
english_stopwords = stopwords.words('english')
tokens_wo_stopwords = [t for t in tokens if t not in english_stopwords]
print("\nText without stop words:", " ".join(tokens_wo_stopwords))