n,a = input().split()
m = list(map(int,input().split()))
x = int(input())
result = None
for i in m:
    if i == x:
        result = "yes"
        break
    else:
        result = "no"
print(result)