from collections import deque
import sys
input = sys.stdin.readline
 
n, m = map(int, input().split()) # 사다리 수, 뱀 수
 
board = [0] * 101
visited = [False] * 101
 
ladder = dict()
for _ in range(n):
    i,j = map(int,input().split())
    ladder[i] = j
 
snack = dict()
for _ in range(m):
    i,j = map(int,input().split())
    snack[i] = j
 
def bfs(start):
    q = deque()
    q.append(start)
 
    visited[start] = True
 
    while q:
        cur = q.popleft()
 
        for i in range(1, 7): # 주사위 1 ~ 6
            next = cur + i
 
            if 0 < next <= 100 and not visited[next]:
                if next in ladder:
                    next = ladder[next]
                
                if next in snack:
                    next = snack[next]
                
                if not visited[next]:
                    q.append(next)
                    visited[next] = True
                    board[next] = board[cur] + 1
 
bfs(1) # 1부터 시작
print(board[100])
