from collections import deque

row, col = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

queue = deque()
maze = []
J = ''
F = []

distance_J = [[-1]*col for _ in range(row)]
distance_F = [[-1]*col for _ in range(row)]
outcase = False

for i in range(row):
    road = input()
    for j in range(col):
        if road[j] == "J":
            J = (i, j, True)
            if i == row - 1 or j == col - 1 or j == 0 or i == 0:
                outcase = True
            distance_J[i][j] = 0
        elif road[j] == "F":
            F.append((i, j, False))
            distance_F[i][j] = 0
        elif road[j] == "#":
            distance_J[i][j] = 0
            distance_F[i][j] = 0
    maze.append([r for r in road])

queue.append(J)
for f in F:
    queue.append(f)

while queue:
    #print(queue)
    cur_x, cur_y, flag = queue.popleft()
    if flag and distance_F[cur_x][cur_y] == distance_J[cur_x][cur_y]:
        distance_J[cur_x][cur_y] = -1
        continue
    for dir in range(4):
        nx, ny = cur_x + dx[dir], cur_y + dy[dir]
        if nx < 0 or ny < 0 or nx >= row or ny >= col:
            continue
        #지훈이를 움직이는 경우
        if flag:
            if distance_J[nx][ny] >= 0 or distance_F[nx][ny] >= 0:
               continue
            distance_J[nx][ny] = distance_J[cur_x][cur_y] + 1
        else:
            if distance_F[nx][ny] >= 0:
               continue
            distance_F[nx][ny] = distance_F[cur_x][cur_y] + 1
        queue.append((nx, ny, flag))

time = 0

distance_exit = []
for i in range(1, row-1):
    distance_exit += [distance_J[i][0]] + [distance_J[i][-1]]
positive_values = filter(lambda x: x > 0, distance_J[0]+distance_J[-1]+distance_exit)
time = min(positive_values, default = -1)

if outcase:
    print(1)
elif time == -1:
    print("IMPOSSIBLE")
else:
    print(time+1)