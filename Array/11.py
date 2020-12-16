lst = list(map(int, input().strip()))
odd_lst = []
for i in lst:
    if i % 2 != 0:
        odd_lst.append(i)
if odd_lst:
    print(*odd_lst)
else:
    print(-1)