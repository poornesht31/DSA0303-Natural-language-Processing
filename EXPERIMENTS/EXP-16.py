from nltk.corpus import wordnet

synsets = wordnet.synsets("car")

for s in synsets[:2]:
    print(s.name(), ":", s.definition())