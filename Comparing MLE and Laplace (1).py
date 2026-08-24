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
    words.extend(sentence.lower().split())

freq = Counter(words)

total = len(words)
vocab = len(freq)

word = input("Enter word: ").lower()

mle = freq[word] / total
laplace = (freq[word] + 1) / (total + vocab)

print("Count =", freq[word])
print("MLE =", round(mle, 4))
print("Laplace =", round(laplace, 4))
