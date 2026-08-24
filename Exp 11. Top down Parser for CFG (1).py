grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"], ["Pronoun"], ["Det", "N", "PP"]],
    "VP": [["V", "NP"], ["V", "NP", "PP"]],
    "PP": [["P", "NP"]],
    "Det": [["the"], ["a"]],
    "N": [["cat"], ["mouse"], ["boy"], ["book"], ["man"], ["telescope"]],
    "V": [["sees"], ["reads"], ["saw"]],
    "P": [["with"]],
    "Pronoun": [["I"]]
}

def parse(symbol, words, pos):
    if symbol not in grammar:
        if pos < len(words) and symbol == words[pos]:
            return pos + 1
        return None

    for rule in grammar[symbol]:
        p = pos

        for item in rule:
            p = parse(item, words, p)

            if p is None:
                break

        if p is not None:
            return p

    return None

sentence = input("Enter sentence: ").lower()
words = sentence.split()

result = parse("S", words, 0)

if result == len(words):
    print("Sentence Accepted")
else:
    print("Sentence Rejected")