# 6 4
# 0100
# 1110
# 1000
# 0000
# 0111
# 0000

# -> 15

# 4 4
# 0111
# 1111
# 1111
# 1110

# -> -1

from collections import deque

queue = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())

matrix = []

for _ in range(N):
    line = input()
    matrix.append(list(line))

queue = deque()
distance = [[[-1, -1] for _ in range(M)] for _ in range(N)]

queue.append((0, 0, False))
distance[0][0][0] = 1

while queue:
    cur_x, cur_y, is_crushed = queue.popleft()

    for dir in range(4):
        nx, ny = cur_x + dx[dir], cur_y + dy[dir]

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        
        if is_crushed:
            if distance[nx][ny][1] > 0 or matrix[nx][ny] == "1":
                continue
            
            distance[nx][ny][1] = distance[cur_x][cur_y][1] + 1
            queue.append((nx, ny, True))
        else:
            if matrix[nx][ny] == "1":
                nnx, nny = nx + dx[dir], ny + dy[dir]
                if nnx < 0 or nny < 0 or nnx >= N or nny >= M:
                    continue
                if distance[nnx][nny][1] > 0 or matrix[nnx][nny] == "1":
                    continue

                distance[nnx][nny][1] = distance[cur_x][cur_y][0] + 2
                queue.append((nnx, nny, True))
            else:
                if distance[nx][ny][0] > 0:
                    continue

                distance[nx][ny][0] = distance[cur_x][cur_y][0] + 1
                queue.append((nx, ny, False))
    
    if distance[N-1][M-1][1] > 0:
        print(distance[N-1][M-1][1])
        break
    elif distance[N-1][M-1][0] > 0:
        print(distance[N-1][M-1][0])
        break

if distance[N-1][M-1][0] < 0 and distance[N-1][M-1][1] < 0:
    print(-1)