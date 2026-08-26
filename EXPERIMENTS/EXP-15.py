import spacy

nlp = spacy.load("en_core_web_sm")

text = "Google is located in California."
doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)