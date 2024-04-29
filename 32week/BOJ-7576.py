# 6 4
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 1

# 6 4
# 0 -1 0 0 0 0
# -1 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 1
from collections import deque

col, row = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

field = []
queue = deque()
distance = [[-1] * col for _ in range(row)]

#입력 처리
for i in range(row):
    tomato = input().split()
    field.append(tomato)
    for t in range(col):
        if tomato[t] == "1":
            queue.append((i, t))
            distance[i][t] = 0
        elif tomato[t] == "-1":
            distance[i][t] = 0

if not queue:
    flag = False
#토마토 익는 것 구현
while queue:
    #현재 큐에 있는 것들은 time 0인 상태임
    #이제 큐에서 하나씩 BFS로 순회하면서 영역을 넓히고
    #다 하면 time++
    cur_x, cur_y = queue.popleft()
    for dir in range(4):
        nx, ny = int(cur_x) + dx[dir], int(cur_y) + dy[dir]
        if nx < 0 or ny < 0 or nx >= row or ny >= col:
            continue
        if distance[nx][ny] >= 0:
            continue
        distance[nx][ny] = distance[cur_x][cur_y] + 1
        queue.append((nx, ny))

time = 0
flag = True
for i in range(row):
    for j in range(col):
        if distance[i][j] == -1:
            flag = False
            break
        time = max(time, distance[i][j])
if flag:
    print(time)
else:
    print(-1)