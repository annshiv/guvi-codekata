n = int(input())
a = list(map(int,input().split(" ")))
b = int(input())
c = list(map(int,input().split(" ")))
output = []
for i in c:
    if i in a:
        output.append(a.count(i))
    else:
        output.append("Not Present")
print(*output)
