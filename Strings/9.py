s = list(map(str,input().split()))

word = 'the'
lst = []
a = s.count("a") + s.count("an") + s.count("The") + s.count("the")

for i in range(len(s)):
    if "The" in s:
        k = s.index("The")
        lst.append(s[k+1])
    if "the" in s:
        l = s.index("the")
        lst.append(s[l+1])
    if "an" in s:
        l = s.index("an")
        lst.append(s[l+1])
    if "a" in s:
        l = s.index("a")
        lst.append(s[l+1])


if len(lst) > 0:
    print(" ".join(lst[:a]))
else:
    print("-1")