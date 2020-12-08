from collections import defaultdict
n = int(input())
m = list(map(int,input().split()))
d = defaultdict(int)
for i in m:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

count = 0
for i in d:
    if d[i] == 1:
        count = i

print(count)