import nltk

train = [[("I", "PRP"), ("run", "VBP")],
         [("He", "PRP"), ("runs", "VBZ")]]

tagger = nltk.UnigramTagger(train)

print(tagger.tag(["I", "run"]))