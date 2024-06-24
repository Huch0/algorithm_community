a=input()
b=input()
c=input()

def ans(num):
    if num%3==0:
        if num%5==0:
            print("FizzBuzz")
        else:
            print("Fizz")
    else:
        if num%5==0:
            print("Buzz")
        else:
            print(num)

if a.isdigit():
    a=int(a)+3
    ans(a)
elif b.isdigit():
    b=int(b)+2
    ans(b)
else:
    c=int(c)+1
    ans(c)