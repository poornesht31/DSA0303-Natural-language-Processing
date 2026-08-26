import random

text = "I like natural language processing"
words = text.split()

bigrams = list(zip(words, words[1:]))

print("Bigrams:")
for b in bigrams:
    print(b)