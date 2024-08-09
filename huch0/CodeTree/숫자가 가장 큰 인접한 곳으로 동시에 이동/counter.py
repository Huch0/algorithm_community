from collections import defaultdict

n, m, t = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

beads = []
for _ in range(m):
    beads.append(tuple(map(lambda x: int(x) - 1, input().split())))

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for time in range(t):
    new_beads = defaultdict(int)
    # Move beads
    for r, c in beads:
        max_nx, max_ny = r, c
        max_num = 0

        for dx, dy in directions:
            nx, ny = r + dx, c + dy

            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] > max_num:
                    max_nx, max_ny = nx, ny
                    max_num = grid[nx][ny]

        new_beads[(max_nx, max_ny)] += 1

    # Eliminate overlapping beads
    beads = [beads for beads, n in new_beads.items() if n == 1]

# Count the number of remaining beads
print(len(beads))
