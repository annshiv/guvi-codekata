from collections import defaultdict
n = int(input())
lst = list(map(int,input().split()))
d = defaultdict(int)
for i,j in enumerate(lst):
    d[j] = i
index_list = []
b = dict(sorted(d.items(),key=lambda x: x[0],reverse=True))
for i in b:
    index_list.append(b[i])
print(*index_list)