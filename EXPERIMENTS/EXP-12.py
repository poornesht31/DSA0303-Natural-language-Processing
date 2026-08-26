import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> 'John'
VP -> 'runs'
""")

parser = nltk.ChartParser(grammar)

for tree in parser.parse("John runs".split()):
    tree.pretty_print()