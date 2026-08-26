import nltk

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger_eng")

text = "The cat runs fast."
words = nltk.word_tokenize(text)

print(nltk.pos_tag(words))