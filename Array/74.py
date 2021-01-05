n,k = map(int,input().split())
lst = list(map(int,input().split()))
if k not in lst:
    print(-1)
else:
    print(lst.count(k)-1)