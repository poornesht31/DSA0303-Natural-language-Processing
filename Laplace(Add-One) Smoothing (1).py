from collections import Counter

corpus = [
    "I love NLP",
    "I love Python",
    "I study NLP",
    "We study Python",
    "You love NLP",
    "I study Python"
]

words = []

for sentence in corpus:
    words.extend(sentence.split())

freq = Counter(words)

total = len(words)
vocab = len(freq)

word = input("Enter word: ")

count = freq[word]

prob = (count + 1) / (total + vocab)

print("Count =", count)
print("Vocabulary Size =", vocab)
print("Laplace Probability =", round(prob,4))
