n,m = input().split()
n = int(n)
m = int(m)
k = list(map(int,input().split(" ")))
if m in k:
    print("yes")
else:
    print("no")