#백준 14500
#테트로미노

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)] # 입력값 저장
visited = [[False] * m for _ in range(n)] # 방문확인

# 방향설정
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

maximum = 0 # 최댓값 저장 변수

# ㅗ 모양을 제외한 나머지 모양 탐색
def dfs(x, y, tmp, cnt):
    global maximum
    if cnt == 4: # 탐색완료 후 최댓값 비교
        maximum = max(maximum, tmp)
        return
    for i in range(4): # 방향 탐색
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=m or ny<0 or ny>=n or visited[ny][nx]:
            continue
        visited[ny][nx] = True # 방문처리
        dfs(nx, ny, tmp+graph[ny][nx], cnt+1)
        visited[ny][nx] = False # 방문처리 제거

# ㅗ 모양 탐색
def fy(x, y):
    global maximum
    tmp = graph[y][x]
    arr = []
    for i in range(4): # 모든 방향 탐색
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=m or ny<0 or ny>=n:
            continue
        arr.append(graph[ny][nx])
    length = len(arr)
    if length == 4 : # 만약 4방향 모두 nxm에 들어간다면 그중 가장 작은 값 제거 후 sum
        arr.sort(reverse=True)
        arr.pop()
        maximum = max(maximum, sum(arr) + graph[y][x])
    elif length == 3: # 3방향만 nxm에 들어가기 때문에 바로 sum
        maximum = max(maximum, sum(arr) + graph[y][x])
    return # length가 2 이하라면 ㅗ 모양이 아니므로 바로 return

for i in range(n):
    for j in range(m):
        visited[i][j] = True # 현재 지점 방문처리
        dfs(j, i, graph[i][j], 1)
        fy(j, i)
        visited[i][j] = False

print(maximum) # 정답 출력
