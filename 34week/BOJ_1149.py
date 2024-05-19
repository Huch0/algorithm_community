# 3
# 26 40 83
# 49 60 57
# 13 89 99

N = int(input())

houses = []

for i in range(N):
    line = input().split()
    line = [int(l) for l in line]
    houses.append(line)

D = [[0, 0, 0] for _ in range(N)]
D[0][0] = houses[0][0]
D[0][1] = houses[0][1]
D[0][2] = houses[0][2]

for i in range(1, N):
    for j in range(3):
        D[i][j] = min(D[i-1][(j+1)%3], D[i-1][(j+2)%3]) + houses[i][j]

print(min(D[N-1][0], D[N-1][1], D[N-1][2]))