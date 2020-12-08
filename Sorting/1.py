n = int(input())
total = []
for i in range(n):
    a = int(input())
    b = list(map(int,input().split()))
    b.sort()
    total += b
print(*total)