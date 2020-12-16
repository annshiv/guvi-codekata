n = int(input())
a = list(map(int,input().split(" ")))
b = list(set(a))
ans_lst = []
for i in b:
    if a.count(i) == 1:
        ans_lst.append(i)

ans_lst.sort(reverse=True)
print(*ans_lst)