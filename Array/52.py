n,k = map(int,input().split())
lst = list(map(int,input().split()))
a = [x for x in lst if x < k]
if a:
    a.sort()
    print(*a)
else:
    print(-1)