import nltk

grammar = nltk.PCFG.fromstring("""
S -> NP VP [1.0]

NP -> Det N [0.6]
NP -> Pronoun [0.2]
NP -> Det N PP [0.2]

VP -> V NP [0.7]
VP -> V NP PP [0.3]

PP -> P NP [1.0]

Det -> 'the' [0.5]
Det -> 'a' [0.5]

N -> 'cat' [0.2]
N -> 'mouse' [0.2]
N -> 'boy' [0.2]
N -> 'book' [0.2]
N -> 'man' [0.1]
N -> 'telescope' [0.1]

V -> 'sees' [0.3]
V -> 'reads' [0.3]
V -> 'saw' [0.4]

P -> 'with' [1.0]

Pronoun -> 'I' [1.0]
""")

sentence = input("Enter sentence: ").lower().split()

parser = nltk.ViterbiParser(grammar)

for tree in parser.parse(sentence):
    print(tree)