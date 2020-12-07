s = input()
result = ""
for i in s:
    r = s.count(i)
    if r == 1:
        result += i
print(result)