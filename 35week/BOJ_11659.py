# 5 3
# 5 4 3 2 1
# 1 3
# 2 4
# 5 5

N, M = map(int, input().split())

line = input().split()
nums = [int(n) for n in line]

D = [0 for _ in range(N+1)]

for i in range(1, N+1):
    D[i] = D[i-1] + nums[i-1]

result = []

for _ in range(M):
    x, y = map(int, input().split())
    result.append(D[y] - D[x-1])

for r in result:
    print(r)