n = int(input())
a = list(map(int,input().split()))
b = list(set(a))
max_count = 0
max_value = 0
for i in b:
    if a.count(i) > max_count:
        max_count = a.count(i)
        max_value = i
print(max_value)