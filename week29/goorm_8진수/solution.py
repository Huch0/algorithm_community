n = int(input())
nums = list(map(int, input().split()))

sum = 0

for num in nums:
    sum += num

octs = []

while(sum > 0):
    octs.append(sum % 8)
    sum = sum // 8

while octs:
    print(octs.pop(), end='')