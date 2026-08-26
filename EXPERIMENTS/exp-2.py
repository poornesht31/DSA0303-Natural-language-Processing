def accepts(s):
    return s.endswith("ab")

for s in ["ab", "aab", "abc", "abab"]:
    print(s, accepts(s))
