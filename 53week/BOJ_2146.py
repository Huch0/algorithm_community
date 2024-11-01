# 10
# 1 1 1 0 0 0 0 1 1 1
# 1 1 1 1 0 0 0 0 1 1
# 1 0 1 1 0 0 0 0 1 1
# 0 0 1 1 1 0 0 0 0 1
# 0 0 0 1 0 0 0 0 0 1
# 0 0 0 0 0 0 0 0 0 1
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 1 1 0 0 0 0
# 0 0 0 0 1 1 1 0 0 0
# 0 0 0 0 0 0 0 0 0 0

# -> 3

# 5
# 1 0 0 0 0
# 0 0 0 0 0
# 0 0 1 0 0
# 0 0 0 0 1
# 0 0 0 0 1

# -> 2

from collections import deque

earth = []

N = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def OOB(nx, ny):
    return nx < 0 or ny < 0 or nx >= N or ny >= N

def print_earth():
    for line in earth:
        for e in line:
            print(e, end = " ")
        print()

for i in range(N):
    line = list(map(int, input().split()))
    earth.append(line)

queue = deque()
is_visited = [[False for _ in range(N)] for _ in range(N)]

# 땅 구별하기
# 1으로 시작하여 새로운 땅을 만날 때마다 2부터 칠하고 3,4,5,,,로 늘리겠다



land = 2
for i in range(N):
    for j in range(N):
        if earth[i][j] == 1:
            earth[i][j] = land
            queue.append((i, j))
            is_visited[i][j] = True
            while queue:
                cur_x, cur_y = queue.popleft()

                for dir in range(4):
                    nx, ny = cur_x + dx[dir], cur_y + dy[dir]
                    
                    if OOB(nx,ny):
                        continue
                    elif earth[nx][ny] == 0 or is_visited[nx][ny]:
                        continue
                    else:
                        earth[nx][ny] = land
                        queue.append((nx, ny))
                        is_visited[nx][ny] = True
            land += 1

t = 0
is_meet = False
while not is_meet:
    # 이제 해결해야 하는 문제는 언제 T를 늘리나?
    cur_land = 2
    t += 1
    meet_pair = []
    for x in range(N):
        for y in range(N):
            meet_value = 0
            

            if earth[x][y] == cur_land:
                cur_land += 1
                queue.append((earth[x][y], x, y))
                is_visited = [[False for _ in range(N)] for _ in range(N)]
                # 땅 넓히기
                while queue:
                    value, cur_x, cur_y = queue.popleft()
                    for dir in range(4):
                        nx, ny = cur_x + dx[dir], cur_y + dy[dir]
                        
                        if OOB(nx,ny):
                            continue
                        elif is_visited[nx][ny]:
                            continue
                        
                        if earth[nx][ny] == value:
                            queue.append((value, nx, ny))
                            is_visited[nx][ny] = True
                        elif earth[nx][ny] == 0:
                            earth[nx][ny] = value
                            is_visited[nx][ny] = True
                        else:
                            is_visited[nx][ny] = True
                            is_meet = True
                            meet_value = max(meet_value, earth[nx][ny])
                            if (meet_value, value) not in meet_pair:
                                meet_pair.append((meet_value, value))
                            # queue.clear()
                            # break
                    
                if not is_meet and cur_land == land:
                    t += 1
    if is_meet:
        # print(meet_pair)
        # print_earth()
        for p in meet_pair:
            # print(p)
            if p[0] > p[1]:
                t -= 1
                break
    if is_meet:
        break
                

# print_earth()
print(t)