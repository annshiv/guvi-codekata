n = int(input())
lst = list(map(str,input().split(" ")))
d = dict()
for i in range(0,len(lst),2):
    d[lst[i]] = lst[i+1]
a = sorted(d.items(),key=lambda x: x[1])
for i in a:
    print(i[0])