n = int(input())
lst = list(map(int,input().split()))
a = list(set(lst))
result = []

for i in a:
    if lst.count(i) == 1:
        result.append(i)
    if lst.count(i) == n:
        result.append(i)
result.sort(reverse=True)
print(*result)