# 5
# 4 3
# ####
# #*@.
# ####
# 7 6
# ###.###
# #*#.#*#
# #.....#
# #.....#
# #..@..#
# #######
# 7 4
# ###.###
# #....*#
# #@....#
# .######
# 5 5
# .....
# .***.
# .*@*.
# .***.
# .....
# 3 3
# ###
# #@#
# ###

from collections import deque

T = int(input())
results = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(T):
    result = 0

    w, h = map(int, input().split())
    
    buliding = []
    sang = []
    fires = []

    for i in range(h):
        line = list(input())
        for j in range(w):
            if line[j] == "@":
                sang = [i, j]
            elif line[j] == "*":
                fires.append([i, j])
        buliding.append(line)
    
    queue = deque()
    distance = [[-1 for _ in range(w)] for _ in range(h)]
    for f in fires:
        queue.append((f[0], f[1], True))
    queue.append((sang[0], sang[1], False))
    distance[sang[0]][sang[1]] = 0

    while queue:
        cur_x, cur_y, is_fire = queue.popleft()
        

        for dir in range(4):
            nx, ny = cur_x + dx[dir], cur_y + dy[dir]

            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            
            if buliding[nx][ny] == "#" or buliding[nx][ny] == "*":
                continue

            if is_fire:
                #if distance[nx][ny] == distance[cur_x][cur_y]:
                buliding[nx][ny] = "*"    
                queue.append((nx, ny, True))

            else: 
                if distance[nx][ny] >= 0:
                    continue
                distance[nx][ny] = distance[cur_x][cur_y] + 1
                queue.append((nx, ny, False))
                # 탈출 가능
                if nx == 0 or nx == h-1 or ny == 0 or ny == w-1:
                    result = distance[nx][ny]

        if result > 0:
            break

    if result == 0 and not(sang[0] == 0 or sang[1] == 0 or sang[0] == h-1 or sang[1] == w-1):
        result = "IMPOSSIBLE"
    else:
        result += 1
    results.append(result)

for r in results:
    print(r)