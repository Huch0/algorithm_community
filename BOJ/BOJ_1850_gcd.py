def gcd(x,y):
    if x < y : x,y = y,x
    
    while x % y != 0:
        temp = y
        y = x % y
        x = temp
    return y

a, b = map(int, input().split())

print("1" * gcd(a,b))