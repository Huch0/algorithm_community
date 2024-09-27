# 5 7
# 0 0 0 0 0 0 0
# 0 2 4 5 3 0 0
# 0 3 0 2 5 2 0
# 0 7 6 2 4 0 0
# 0 0 0 0 0 0 0

from collections import deque

N, M = map(int, input().split())
iceberg = []

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def count_ice():
    return sum([1 for ice in iceberg for i in ice if i > 0])

def count_visit():
    return sum([1 for line in visited for val in line if val])

def choose_ice():
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] > 0:
                return (i, j)
    # if there isn't ice
    return (-1, -1)

for _ in range(N):
    ice = list(map(int, input().split()))
    iceberg.append(ice)

# def print_iceberg():
#     for ice in iceberg:
#         for i in ice:
#             print(i, end = " ")
#         print()

step = 0
while True:
    n_ice = count_ice()
    queue = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]

    p_ice = choose_ice()
    if p_ice == (-1, -1):
        step = 0
        break
    queue.append(p_ice)
    visited[p_ice[0]][p_ice[1]] = True

    while queue:
        cur_x, cur_y = queue.pop()

        for dir in range(4):
            nx, ny = cur_x + dx[dir], cur_y + dy[dir]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if visited[nx][ny]:
                continue
            if iceberg[nx][ny] == 0:
                if iceberg[cur_x][cur_y] > 0:
                    iceberg[cur_x][cur_y] -= 1
            if iceberg[nx][ny] > 0:
                queue.append((nx, ny))
                visited[nx][ny] = True
    
    n_visit = count_visit()
    # print(f"{n_ice} / {n_visit}")
    # print_iceberg()
    if n_ice != n_visit:
        break
    step += 1

print(step)