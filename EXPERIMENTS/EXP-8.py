import nltk

patterns = [
    (r".*ing$", "VBG"),
    (r".*ed$", "VBD"),
    (r".*ly$", "RB"),
    (r".*", "NN")
]

tagger = nltk.RegexpTagger(patterns)

print(tagger.tag(["playing", "walked", "quickly", "book"]))