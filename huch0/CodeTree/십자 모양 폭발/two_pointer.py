n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

r, c = map(int, input().split())
r, c = r - 1, c - 1

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# Burst the bomb
dist = grid[r][c]
grid[r][c] = 0
for d in range(1, dist):
    for dx, dy in directions:
        nx, ny = r + dx * d, c + dy * d

        if 0 <= nx < n and 0 <= ny < n:
            grid[nx][ny] = 0

# Bomb rain
for col in range(n):
    down = -1
    for up in range(-1, -n - 1, -1):
        if grid[down][col] > 0:
            down -= 1
            continue

        if grid[up][col] > 0:
            grid[down][col], grid[up][col] = grid[up][col], 0
            down -= 1


for i in range(n):
    print(' '.join(map(str, grid[i])))
