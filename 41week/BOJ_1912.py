# 10
# 10 -4 3 1 5 6 -35 12 21 -1
# -> 33

# 10
# 2 1 -4 3 4 -4 6 5 -5 1
# -> 14

# 5
# -1 -2 -3 -4 -5
# -> -1

N = int(input())

line = list(map(int, input().split()))

D = [[0, 0] for _ in range(N)]

D[0][0] = line[0]
D[0][1] = line[0]

for i in range(1, len(line)):
    D[i][1] = max(0, D[i-1][1]) + line[i]
    D[i][0] = max(D[i-1][0], D[i][1])

print(D[N-1][0])