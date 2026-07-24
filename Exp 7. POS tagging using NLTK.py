import nltk
from nltk.tokenize import word_tokenize

text = input("Enter sentence: ")

words = word_tokenize(text)

print(nltk.pos_tag(words))
