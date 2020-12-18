n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
x = list(set(a))
com_ele = []
for i in x:
    if i in b:
        com_ele.append(i)
if com_ele:
    print(*com_ele)
else:
    print(-1)