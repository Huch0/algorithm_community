import sys
import heapq

INF = 987654321
DIRECTIONS = {(1, 0), (0, 1), (-1, 0), (0, -1)}

m, n = map(int, sys.stdin.readline().split())
adjMatrix = [[1 for _ in range(n)] for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]
hMatrix = [[INF for _ in range(n)] for _ in range(m)]

grayCellsNum = int(input())

for _ in range(grayCellsNum):
    _, x, y = map(int, sys.stdin.readline().split())
    adjMatrix[x][y] = 0

user_input = input()
_, x, y = user_input.split()
x, y = int(x), int(y)
start = (x, y)

user_input = input()
_, x, y = user_input.split()
x, y = int(x), int(y)
goal = (x, y)

user_input = input()
_, obNum = user_input.split()
obNum = int(obNum)

for _ in range(obNum):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for j in range(x1, x2 + 1):
        for k in range(y1, y2 + 1):
            adjMatrix[j][k] = 0

def hFunc(x, y):
    global goal
    a = abs(x - goal[0])
    b = abs(y - goal[1])
    return a + b

def a_star(start, goal):
    pq = [(hFunc(*start), 0, start)]  # (priority, cost, position)
    visited[start[0]][start[1]] = True
    
    while pq:
        current_cost, cost, (x, y) = heapq.heappop(pq)
        if (x, y) == goal:
            return cost
        
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and adjMatrix[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                next_cost = cost + 1  # Assuming each move has a cost of 1
                heapq.heappush(pq, (next_cost + hFunc(nx, ny), next_cost, (nx, ny)))
                
    return INF  # Goal is not reachable

# Calculate the cost and multiply by 3 as per original requirement
cost = a_star(start, goal)
print(cost * 3 if cost != INF else -1)


   
        
