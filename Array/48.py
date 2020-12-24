n = int(input())
lst = list(map(str,input().split()))
max_value = 0
max_count = 0
a = list(set(lst))
for i in a:
    if lst.count(i) > max_count:
        max_count = lst.count(i)
        max_value = i
print(max_value)