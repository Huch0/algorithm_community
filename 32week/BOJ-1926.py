# 6 5
# 1 1 0 1 1
# 0 1 1 0 0
# 0 0 0 0 0
# 1 0 1 1 1
# 0 0 1 1 1
# 0 0 1 1 1

row, col = input().split()
row, col = int(row), int(col)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

painting = []
visit = [[False] * col for _ in range(row)]
#입력 처리
for i in range(row):
    painting.append(input().split())
    
#그림 카운팅
count = 0
area = 0

for i in range(row):
    for j in range(col):
        if painting[i][j] == "1" and not visit[i][j]:
            x, y = i, j
        else:
            continue
        queue = [(x, y)]
        visit[x][y] = True
        
        cur_area = 0
        while queue:
            cur_x, cur_y = queue.pop(0)
            cur_area += 1

            for dir in range(4):
                nx = cur_x + dx[dir]
                ny = cur_y + dy[dir]

                if nx < 0 or ny < 0 or nx >= row or ny >= col:
                    continue
                if not visit[nx][ny] and painting[nx][ny] == "1":
                    queue.append((nx, ny))
                    visit[nx][ny] = True
        count += 1
        if area < cur_area:
            area = cur_area

print(count, area)