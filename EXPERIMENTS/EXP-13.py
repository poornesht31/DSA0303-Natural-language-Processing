def check(sentence):
    words = sentence.split()

    if words[0] in ["He", "She"] and words[1] == "run":
        return "No agreement"
    return "Agreement is correct"

print(check("He runs"))
print(check("He run"))