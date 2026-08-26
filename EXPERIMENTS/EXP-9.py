tags = [("I", "NN"), ("am", "NN"), ("happy", "NN")]

for word, tag in tags:
    if word == "I":
        tag = "PRP"
    elif word == "am":
        tag = "VBP"
    print(word, tag)