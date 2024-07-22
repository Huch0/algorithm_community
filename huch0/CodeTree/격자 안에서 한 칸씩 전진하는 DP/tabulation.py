N = int(input())
mat = []
for _ in range(N):
    mat.append(list(map(int, input().split())))

table = [[0] * N for _ in range(N)]
s = table[0][0] = mat[0][0]

for i in range(1, N):
    s += mat[i][0]
    table[i][0] = s

s = table[0][0]
for j in range(1, N):
    s += mat[0][j]
    table[0][j] = s

for i in range(1, N):
    for j in range(1, N):
        table[i][j] = max(table[i - 1][j], table[i][j - 1]) + mat[i][j]

print(table[N - 1][N - 1])
