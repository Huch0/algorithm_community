from collections import deque

def solution(n, m, hole):
    answer = 0
    queue = deque()

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    distance = [[[-1,-1] for _ in range(n)] for _ in range(m)]
    for h in hole:
        distance[m-h[1]][h[0]-1] = [0,0]
    
    distance[m-1][0] = [0,-1]
    queue.append((m-1, 0, 0))
    while queue:
        cur_x, cur_y, jump = queue.popleft()

        for dir in range(4):
            nx, ny = cur_x + dx[dir], cur_y + dy[dir]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if jump:
                if distance[nx][ny][1] >= 0:
                    continue
                distance[nx][ny] = [distance[nx][ny][0], distance[cur_x][cur_y][1]+1]
                queue.append((nx, ny, jump))
            else:
                nnx, nny = nx + dx[dir], ny + dy[dir]
                if 0 <= nnx and nnx < m and 0 <= nny and nny < n:
                    if distance[nnx][nny][1] < 0 and distance[nnx][nny][0] < 0:
                        distance[nnx][nny] = [distance[nnx][nny][0], distance[cur_x][cur_y][0]+1]
                        queue.append((nnx, nny, 1))
                if distance[nx][ny][0] >= 0:
                    continue
                distance[nx][ny] = [distance[cur_x][cur_y][0] + 1, distance[nx][ny][1]]
                queue.append((nx, ny, jump))
        if distance[0][n-1][1] > 0:
            answer = distance[0][n-1][1]
    if answer == 0:
        return -1
    return answer