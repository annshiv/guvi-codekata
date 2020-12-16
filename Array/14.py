n = int(input())
a = list(map(str,input().split(" ")))
b = []
for i in a:
    if i not in b:
        b.append(i)
print(*b)