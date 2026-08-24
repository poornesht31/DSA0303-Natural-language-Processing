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
bigrams = []

for sentence in corpus:
    w = sentence.split()

    words.extend(w)

    for i in range(len(w)-1):
        bigrams.append((w[i],w[i+1]))

uni = Counter(words)
bi = Counter(bigrams)

vocab = len(uni)

w1 = input("First word: ")
w2 = input("Second word: ")

count_bigram = bi[(w1,w2)]
count_word = uni[w1]

prob = (count_bigram+1)/(count_word+vocab)

print("Bigram Count =",count_bigram)
print("Probability =",round(prob,4))
