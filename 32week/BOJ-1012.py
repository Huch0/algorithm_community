from collections import deque

T = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

result = []

for _ in range(T):
    col, row, K = map(int, input().split())
    field = [[0] * col for _ in range(row)]
    queue = deque()
    visit = [[False] * col for _ in range(row)]
    for i in range(K):
        y, x = map(int, input().split())
        field[x][y] = 1

    count = 0

    for i in range(row):
        for j in range(col):
            if field[i][j] == 1 and not visit[i][j]:
                queue.append((i, j))
                visit[i][j] = True
                count += 1
            while queue:
                cur_x, cur_y = queue.popleft()

                for dir in range(4):
                    nx, ny = cur_x + dx[dir], cur_y + dy[dir]

                    if nx < 0 or ny < 0 or nx >= row or ny >= col:
                        continue
                    if visit[nx][ny] or field[nx][ny] == 0:
                        continue
            
                    queue.append((nx, ny))
                    visit[nx][ny] = True
    result.append(count)

for r in result:
    print(r)