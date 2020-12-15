n,m = input().split()
n = int(n)
m = int(m)
ram = 0
sita = 0
main_lst = []
for _ in range(n):
    lst = list(map(int,input().split()))
    main_lst.append(lst)
for i in range(n):
    for j in range(m):
        if main_lst[i][j] == 0:
            ram += 1
        else:
            sita += 1
print('RAM',ram)
print('SITA',sita)