words = input("Enter words: ").split()

for word in words:
    tag = "NN"

    if word.endswith("ing"):
        tag = "VBG"

    print(word,"->",tag)
