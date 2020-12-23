n = int(input())
lst = list(map(int,input().split()))
neg = []
for i in lst:
    if i < 0:
        neg.append(i)
print(sum(neg))