n = int(input())
a = list(map(int,input().split()))
for i in range(0,len(a)-1,2):
    temp = a[i]
    a[i] = a[i+1]
    a[i+1] = temp
print(*a)