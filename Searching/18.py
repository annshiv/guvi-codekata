n = int(input())
lst = list(map(int,input().split()))
ans_lst = []
i = 0
for j in lst[i:]:
    if max(lst[i:]) == lst[i:][0]:
        ans_lst.append(lst[i:][0])
    i += 1
print(*ans_lst)