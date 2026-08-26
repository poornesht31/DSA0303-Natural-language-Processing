import re

text = "P(x) AND Q(x)"

tokens = re.findall(r"[A-Za-z]+|\(|\)", text)

print(tokens)