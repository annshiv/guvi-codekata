n = int(input())
lst = list(map(int,input().split()))
a = []
for i in lst:
    if i < 0:
        a.append(i)
if len(a) == n:
    print(lst[0])
else:
    print(sum(lst))
