n = int(input())
lst = list(map(int,input().split()))
n = lst.index(max(lst)) + 1
m = lst.index(min(lst)) + 1
print(m,n)