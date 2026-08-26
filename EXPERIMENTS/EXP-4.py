from nltk.stem import PorterStemmer

ps = PorterStemmer()
words = ["running", "easily", "jumps", "studies"]

for w in words:
    print(w, "->", ps.stem(w))