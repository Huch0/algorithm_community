def gcd(x,y):
    if x < y : x,y = y,x
    
    while x % y != 0:
        temp = y
        y = x % y
        x = temp
    return y

for _ in range(int(input())):
    nums = list(map(int,input().split()))
    total = 0
    for i in range(1, len(nums)):
        for j in range(i + 1, len(nums)):
            total += gcd(nums[i], nums[j])
    print(total)