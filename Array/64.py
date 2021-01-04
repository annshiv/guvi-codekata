n,k = map(int,input().split())
lst = list(map(int,input().split()))
for i in range(k):
    l = lst.pop()
    lst.insert(0,l)
print(*lst)
