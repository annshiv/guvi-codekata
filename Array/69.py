n = int(input())
lst = list(map(int,input().split()))
min_count = 0
for i in range(n-1):
    for j in range(i+1,n):
        if lst[j] - lst[i] > min_count:
            min_count = lst[j] - lst[i]
print(min_count)