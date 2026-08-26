import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> 'John'
VP -> 'runs'
""")

parser = nltk.ChartParser(grammar)
sentence = "John runs".split()

for tree in parser.parse(sentence):
    print(tree)