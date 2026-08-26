import spacy

nlp = spacy.load("en_core_web_sm")

text = input("Enter a text: ")

doc = nlp(text)

pronouns = {"he", "she", "it", "they", "him", "her", "them"}

nouns = []

for token in doc:
    if token.pos_ in ["NOUN", "PROPN"]:
        nouns.append(token.text)

print("\nReference Resolution:")

for token in doc:
    if token.text.lower() in pronouns:
        if nouns:
            print(token.text, "->", nouns[-1])
        else:
            print(token.text, "-> Reference not found")
