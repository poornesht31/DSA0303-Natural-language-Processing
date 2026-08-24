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

sentence = input("Enter sentence: ").lower().split()

chart = [[] for _ in range(len(sentence) + 1)]
chart[0].append(("S", ["NP", "VP"], 0, 0))

for i in range(len(sentence) + 1):

    changed = True

    while changed:
        changed = False

        for lhs, rhs, dot, start in chart[i][:]:

            if dot < len(rhs):

                symbol = rhs[dot]

                if symbol in grammar:

                    for rule in grammar[symbol]:
                        item = (symbol, rule, 0, i)

                        if item not in chart[i]:
                            chart[i].append(item)
                            changed = True

                elif i < len(sentence):

                    if symbol.lower() == sentence[i].lower():
                        item = (lhs, rhs, dot + 1, start)

                        if item not in chart[i + 1]:
                            chart[i + 1].append(item)

            else:

                for l, r, d, s in chart[start]:

                    if d < len(r) and r[d] == lhs:
                        item = (l, r, d + 1, s)

                        if item not in chart[i]:
                            chart[i].append(item)
                            changed = True

accepted = ("S", ["NP", "VP"], 2, 0) in chart[len(sentence)]

if accepted:
    print("Sentence Accepted")
else:
    print("Sentence Rejected")