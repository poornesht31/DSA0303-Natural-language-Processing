import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N
NP -> Pronoun
NP -> Det N PP
VP -> V NP
VP -> V NP PP
PP -> P NP

Det -> 'the' | 'a'
N -> 'cat' | 'mouse' | 'boy' | 'book' | 'man' | 'telescope'
V -> 'sees' | 'reads' | 'saw'
P -> 'with'
Pronoun -> 'I'
""")

sentence = input("Enter sentence: ").lower().split()

parser = nltk.ChartParser(grammar)

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()