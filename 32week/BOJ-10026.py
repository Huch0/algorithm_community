# 5
# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR

from collections import deque

N = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

result = []
field = []
for _ in range(N):
    line = input()
    component = []
    for i in range(len(line)):
        if line[i] == "R":
            component.append(0)
        elif line[i] == "G":
            component.append(1)
        else:
            component.append(2)
    field.append(component)

queue = deque()
#처음에는 R과 G를 구분해서 
#두번째는 R이랑 G는 같다로 간다.
target = []
for k in range(2):
    count = 0
    visit = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                target.clear()
                queue.append((i, j))
                visit[i][j] = True
                #target 설정
                if k == 1 and field[i][j] < 2:
                    target = [0, 1]
                else:
                    target.append(field[i][j])
                count += 1
            while queue:
                cur_x, cur_y = queue.popleft()

                for dir in range(4):
                    nx, ny = cur_x + dx[dir], cur_y + dy[dir]

                    if nx < 0 or ny < 0 or nx >= N or ny >= N:
                        continue
                    if visit[nx][ny] or field[nx][ny] not in target:
                        continue
                    queue.append((nx, ny))
                    visit[nx][ny] = True
    result.append(count)

print(str(result[0]) + " " + str(result[1]))