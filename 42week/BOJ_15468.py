# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200

# N = int(input())

# D = [0 for _ in range(1500002)]

# query = []
# for _ in range(N):
#     T, P = map(int, input().split())
#     query.append((T, P))

# for i in range(N, 0, -1):
#     T, P = query[i-1][0], query[i-1][1]
#     if (i + T - 1) <= N:
#         D[i] = max(D[i+T-1] + P, D[i+1])
#     else:
#         D[i] = D[i+1]

# print(D[:N+1])

import sys

input = sys.stdin.readline
N = int(input().strip())
tasks = []

for _ in range(N):
    T, P = map(int, input().strip().split())
    tasks.append((T, P))

D = [0 for _ in range(N+1)]

for i in range(1, N+1):
    T, P = tasks[i-1][0], tasks[i-1][1]
    if (i + T - 1) <= N:
        D[i+T-1] = max(D[i+T-1], D[i-1] + P)
    D[i] = max(D[i], D[i-1])

print(D[N])