lst = list(map(str,input().split()))
n = input()
if n in lst:
    print(lst.count(n))
else:
    print(-1)