#���� 14500
#��Ʈ�ι̳�

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)] # �Է°� ����
visited = [[False] * m for _ in range(n)] # �湮Ȯ��

# ���⼳��
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

maximum = 0 # �ִ� ���� ����

# �� ����� ������ ������ ��� Ž��
def dfs(x, y, tmp, cnt):
    global maximum
    if cnt == 4: # Ž���Ϸ� �� �ִ� ��
        maximum = max(maximum, tmp)
        return
    for i in range(4): # ���� Ž��
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=m or ny<0 or ny>=n or visited[ny][nx]:
            continue
        visited[ny][nx] = True # �湮ó��
        dfs(nx, ny, tmp+graph[ny][nx], cnt+1)
        visited[ny][nx] = False # �湮ó�� ����

# �� ��� Ž��
def fy(x, y):
    global maximum
    tmp = graph[y][x]
    arr = []
    for i in range(4): # ��� ���� Ž��
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=m or ny<0 or ny>=n:
            continue
        arr.append(graph[ny][nx])
    length = len(arr)
    if length == 4 : # ���� 4���� ��� nxm�� ���ٸ� ���� ���� ���� �� ���� �� sum
        arr.sort(reverse=True)
        arr.pop()
        maximum = max(maximum, sum(arr) + graph[y][x])
    elif length == 3: # 3���⸸ nxm�� ���� ������ �ٷ� sum
        maximum = max(maximum, sum(arr) + graph[y][x])
    return # length�� 2 ���϶�� �� ����� �ƴϹǷ� �ٷ� return

for i in range(n):
    for j in range(m):
        visited[i][j] = True # ���� ���� �湮ó��
        dfs(j, i, graph[i][j], 1)
        fy(j, i)
        visited[i][j] = False

print(maximum) # ���� ���