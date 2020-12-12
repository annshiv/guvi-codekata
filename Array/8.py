n,m = input().split()
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a = sorted(a)
b = sorted(b,reverse=True)
result = a + b
print(*result)