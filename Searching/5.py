n,mark = input().split()
n = int(n)
mark = int(mark)
m = list(map(int,input().split()))
answer = None
for i in m:
    if i == mark:
        answer = m.index(i)
        break
    else:
        answer = "-1"

print(answer)