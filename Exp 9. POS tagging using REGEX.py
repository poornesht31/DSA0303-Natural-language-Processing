import re

words = input("Enter words: ").split()

for word in words:
    if re.search("ing$", word):
        print(word,"-> VBG")
    elif re.search("ed$", word):
        print(word,"-> VBD")
    else:
        print(word,"-> NN")
