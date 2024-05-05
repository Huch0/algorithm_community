def solution(land):
    def get_size_of_oil(land, i, j):
        if land[i][j] != 1:
            return 0
        nonlocal leftmost
        nonlocal rightmost

        leftmost = min(leftmost, j)
        rightmost = max(rightmost, j)

        land[i][j] = '-'
        size = 1

        for dx, dy in directions:
            nx, ny = i + dx, j + dy
            if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1:
                size += get_size_of_oil(land, nx, ny)

        return size

    n, m = len(land), len(land[0])
    column_oils = [0] * m
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    leftmost, rightmost = 0, 0

    for i in range(n):
        for j in range(m):
            if land[i][j] != 1:
                continue
            leftmost = rightmost = j
            oils = get_size_of_oil(land, i, j)

            for column in range(leftmost, rightmost + 1):
                column_oils[column] += oils

    return max(column_oils)
