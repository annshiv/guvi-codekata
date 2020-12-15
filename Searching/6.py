m = int(input())
ans_lst = []
for _ in range(m):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for i in a:
        if i not in b:
            ans_lst.append(a.index(i))
for i in ans_lst:
    print(i)