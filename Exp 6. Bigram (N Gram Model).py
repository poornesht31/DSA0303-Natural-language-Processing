from nltk import bigrams

text = input("Enter text: ")

words = text.split()

print(list(bigrams(words)))
