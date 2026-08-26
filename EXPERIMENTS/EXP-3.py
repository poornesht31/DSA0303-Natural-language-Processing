from nltk.stem import PorterStemmer

ps = PorterStemmer()
words = ["playing", "played", "studies"]

for w in words:
    print(w, "->", ps.stem(w))