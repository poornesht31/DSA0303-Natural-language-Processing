import spacy

nlp = spacy.load("en_core_web_sm")

sentence = input("Enter a sentence: ")

doc = nlp(sentence)

print("\nNoun Phrases and Their Meanings:")
for chunk in doc.noun_chunks:
    print("Noun Phrase:", chunk.text)
    print("Root:", chunk.root.text)
    print("Meaning: An entity or concept represented by the noun phrase.")
    print()
