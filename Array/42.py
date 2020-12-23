n = int(input())
lst = list(map(int,input().split()))
a = list(set(lst))
ans = None
for i in a:
    if lst.count(i) > 1:
        ans = i
        break
    else:
        ans = -1
print(ans)