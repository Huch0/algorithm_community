# 3
# 8
# 0 0
# 7 0
# 100
# 0 0
# 30 50
# 10
# 1 1
# 1 1
from collections import deque

T = int(input())
results = []

dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(T):
    result = 0
    I = int(input())
    start_x, start_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())

    queue = deque()
    distance = [[-1 for _ in range(I)] for _ in range(I)]

    queue.append((start_x, start_y))
    distance[start_x][start_y] = 0

    while queue:
        cur_x, cur_y = queue.popleft()

        for dir in range(8):
            nx, ny = cur_x + dx[dir], cur_y + dy[dir]
            
            if nx < 0 or ny < 0 or nx >= I or ny >= I:
                continue
            if distance[nx][ny] >= 0:
                continue
            distance[nx][ny] = distance[cur_x][cur_y] + 1
            queue.append((nx, ny))
        if distance[goal_x][goal_y] >= 0:
            result = distance[goal_x][goal_y]
            break

    results.append(result)

for r in results:
    print(r)