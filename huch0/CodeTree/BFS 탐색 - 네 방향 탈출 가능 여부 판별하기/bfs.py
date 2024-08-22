from collections import deque
n, m = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = set()
terminated = 0
Q = deque([(0, 0)])
while Q:
    x, y = Q.popleft()

    if x == n - 1 and y == m - 1:
        terminated = 1
        break

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if grid[nx][ny] == 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                Q.append((nx, ny))

print(terminated)
