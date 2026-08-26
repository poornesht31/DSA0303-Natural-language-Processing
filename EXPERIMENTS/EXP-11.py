import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> 'John'
VP -> 'runs'
""")

parser = nltk.EarleyChartParser(grammar)

for tree in parser.parse("John runs".split()):
    print(tree)