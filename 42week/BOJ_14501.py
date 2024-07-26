# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200

N = int(input())

D = [0 for _ in range(N+1)]

for i in range(1, N+1):
    T, P = map(int, input().split())
    if (i + T - 1) <= N:
        D[i+T-1] = max(D[i+T-1], D[i-1] + P)
    D[i] = max(D[i], D[i-1])

print(D[N])