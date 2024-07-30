# 5
# 3 1 4 3 2

N = int(input())

moneys = list(map(int, input().split()))
moneys.sort()

D = moneys[::]
for i in range(1, N):
    D[i] += D[i-1]

print(sum(D))