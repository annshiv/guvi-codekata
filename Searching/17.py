n = int(input())
lst = list(map(int,input().split()))
triple = 0
l = list(set(lst))
for i in l:
    if lst.count(i) == 3:
        triple += 1
print(triple)