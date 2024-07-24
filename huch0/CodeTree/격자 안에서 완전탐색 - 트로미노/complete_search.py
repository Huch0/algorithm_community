n, m = map(int, input().split())
mat = []

for _ in range(n):
    mat.append(list(map(int, input().split())))

# *  ** **  *
# ** *   * **
blocks = [((0, 0), (1, 0), (1, 1)), ((0, 0), (0, 1), (1, 0)), ((0, 0), (0, 1), (1, 1)), ((0, 1), (1, 1), (1, 0))]

#     *
#     *
# *** *
blocks += [((0, 0), (0, 1), (0, 2)), ((0, 0), (1, 0), (2, 0))]

max_sum = 0
for i in range(n):
    for j in range(m):
        if i < n - 1 and j < m - 1:
            for block in blocks[:4]:
                s = 0
                for dx, dy in block:
                    nx, ny = i + dx, j + dy
                    s += mat[nx][ny]

                max_sum = max(max_sum, s)

        if j < m - 2:
            s = sum([mat[i][j], mat[i][j + 1], mat[i][j + 2]])
            max_sum = max(max_sum, s)

        if i < n - 2:
            s = sum([mat[i][j], mat[i + 1][j], mat[i + 2][j]])
            max_sum = max(max_sum, s)


print(max_sum)
