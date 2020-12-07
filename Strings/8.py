s = input()
vowel = ['a','e','i','o','u']
ans = ""
for i in vowel:
    for j in s:
        if i in j:
            ans = "yes"
            break

if len(ans) == 0:
    print("no")
else:
    print(ans)