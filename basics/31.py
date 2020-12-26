n,m = map(str,input().split())
if n == m:
    print("D")
elif n == 'P' and m == 'R':
    print(n)
elif n == 'P' and m == 'S':
    print(m)
elif n == 'S' and m == 'R':
    print(m)
elif n == 'S' and m == 'P':
    print(n)
elif n == 'R' and m == 'S':
    print(n)
elif n == 'R' and m == 'P':
    print(m)