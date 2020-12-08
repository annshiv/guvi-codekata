def fact(a):
    value = 1
    for i in range(1,a+1):
        value *= i
    return value

a,b = input().split()
c = int(fact(int(a))/fact(int(b)))
print(c)