n = int(input())
l,r = input().split()
a = [x for x in range(int(l),int(r)+1)]
if n in a:
    print("yes")
else:
    print("no")