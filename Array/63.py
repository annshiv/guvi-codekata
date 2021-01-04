n = int(input())
lst = list(map(int,input().split()))
a = list(set(lst))
for i in a:
    if lst.count(i) == 1:
        print(i)