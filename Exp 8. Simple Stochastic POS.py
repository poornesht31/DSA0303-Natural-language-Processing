words = input("Enter words: ").split()

tags = {
    "I":"PRP",
    "am":"VBP",
    "playing":"VBG",
    "cricket":"NN"
}

for word in words:
    print(word,"->",tags.get(word,"NN"))
