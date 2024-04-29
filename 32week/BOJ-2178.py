# 4 6
# 101111
# 101010
# 101011
# 111011

row, col = input().split()
row, col = int(row), int(col)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

maze = []
distance = [[-1] * col for _ in range(row)]

#입력 처리
for i in range(row):
    road = input()
    maze.append([i for i in road])
    
#그림 카운팅
count = 0

for i in range(row):
    for j in range(col):
        if maze[i][j] == "1" and distance[i][j] < 0:
            x, y = i, j
        else:
            continue
        queue = [(x, y)]
        distance[x][y] = 0
        
        while queue:
            cur_x, cur_y = queue.pop(0)

            for dir in range(4):
                nx = cur_x + dx[dir]
                ny = cur_y + dy[dir]

                if nx < 0 or ny < 0 or nx >= row or ny >= col:
                    continue
                if distance[nx][ny] < 0 and maze[nx][ny] == "1":
                    queue.append((nx, ny))

                    ### 여기 틀릴뻔
                    distance[nx][ny] = distance[cur_x][cur_y] + 1
        
print(distance[row-1][col-1] + 1)

