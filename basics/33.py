a,b = input().split(" ")
a = int(a)
b = int(b)
def gcd(a, b):
    if(a == 0 and b == 0):
        return 0
       
    if(a == 0):
        return b
     
    if(b == 0):
        return a

    if(a == b):
        return a
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)

print(gcd(a,b))