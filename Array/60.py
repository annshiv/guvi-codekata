n = int(input())
lst = list(map(int,input().split()))
max_value = 0
for i in range(len(lst)-1):
    if lst[i] + lst[i+1] > max_value:
        max_value = lst[i] + lst[i+1]
print(max_value)