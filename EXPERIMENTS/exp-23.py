import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download("punkt")

text = input("Enter a text: ")

sentences = nltk.sent_tokenize(text)

if len(sentences) < 2:
    print("Enter at least two sentences.")
else:
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(sentences)

    scores = []

    for i in range(len(sentences) - 1):
        score = cosine_similarity(
            vectors[i], vectors[i + 1]
        )[0][0]
        scores.append(score)

    average = sum(scores) / len(scores)

    print("\nCoherence Scores:")
    for i, score in enumerate(scores):
        print(
            "Sentence", i + 1,
            "and Sentence", i + 2,
            ":", round(score, 3)
        )

    print("\nOverall Coherence Score:", round(average, 3))

    if average >= 0.5:
        print("Result: Highly Coherent")
    elif average >= 0.2:
        print("Result: Moderately Coherent")
    else:
        print("Result: Low Coherence")
