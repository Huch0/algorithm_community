from collections import deque

num_row, num_col = map(int, input().split())
maze = [[0 for _ in range(num_col)] for _ in range(num_row)]

for i in range(num_row):
    line = input()
    for j in range(num_col):
        maze[i][j] = int(line[j])

visited = [[False for _ in range(num_col)] for _ in range(num_row)]
# 방문 표시를 해야한다!!
distance = [[0 for _ in range(num_col)] for _ in range(num_row)]
# 최단경로 문제이므로, distance table을 만들어준다.
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 길찾기 문제에서 자주 쓰이는 패턴. 상하좌우
queue = deque([(0, 0)])
# bfs이므로 deque 이용. 탐색할 노드를 pop, 인접 노드를 push.
visited[0][0] = True

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 미로 범위 내에서만 이동. 방문하지 않은 1로만 이동.
            if 0 <= nx < num_row and 0 <= ny < num_col and not visited[nx][ny] and maze[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1

bfs()
print(distance[num_row - 1][num_col - 1] + 1)





