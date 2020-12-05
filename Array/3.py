n = int(input())
lst = list(map(int,input().split()))
if sum(lst) % 2 == 0 and sum(lst)%3 == 0 and sum%5 == 0:
    print("1")
else:
    print("0")