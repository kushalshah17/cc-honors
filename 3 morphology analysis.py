import spacy
nlp = spacy.load("en_core_web_sm")
interrogative_sentence = "What is the current mileage of the car?"
declarative_sentence = "The car's odometer reading shows 50,000 miles."
complex_sentence = "I planned to take the car for a drive, but it wouldn't start, so I had to call for roadside assistance."
interrogative_doc = nlp(interrogative_sentence)
declarative_doc = nlp(declarative_sentence)
complex_doc = nlp(complex_sentence)
for token in interrogative_doc:
    print(token.text, token.pos_)
print("\n")
for token in declarative_doc:
    print(token.text, token.pos_)
print("\n")
for token in complex_doc:
    print(token.text, token.pos_)






import spacy

nlp = spacy.load("en_core_web_sm")

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return nlp(content)

input_file_path = '/content/ind.txt'
interrogative_doc = process_file(input_file_path)
print("Interrogative Sentence:")
for token in interrogative_doc:
    print(token.text, token.pos_)
print("\n")