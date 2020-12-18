a = int(input())
lst = list(map(int,input().split()))
first = lst[:3]
last = lst[-3:]
if sum(first) == sum(last):
    print(1)
else:
    print(0)