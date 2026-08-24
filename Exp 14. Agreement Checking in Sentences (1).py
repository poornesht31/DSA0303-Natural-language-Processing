subjects = {
    "cat": "singular",
    "boy": "singular",
    "mouse": "singular",
    "book": "singular"
}

singular_verbs = ["sees", "reads"]
plural_verbs = ["see", "read"]

sentence = input("Enter sentence: ").lower().split()

subject = sentence[1]
verb = sentence[2]

if subject in subjects and subjects[subject] == "singular":
    if verb in singular_verbs:
        print("Agreement Correct")
    else:
        print("Agreement Incorrect")

else:
    print("Agreement Incorrect")