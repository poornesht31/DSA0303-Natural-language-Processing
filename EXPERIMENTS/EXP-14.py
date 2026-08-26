import nltk

grammar = nltk.PCFG.fromstring("""
S -> NP VP [1.0]
NP -> 'John' [1.0]
VP -> 'runs' [1.0]
""")

parser = nltk.ViterbiParser(grammar)

for tree in parser.parse("John runs".split()):
    print(tree)