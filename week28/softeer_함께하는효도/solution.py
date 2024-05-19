from itertools import product
from collections import deque
import copy

def bfs_max_fruits(grid, start_positions, time_limit):
    n = len(grid)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 이동
    max_fruits = 0
    
    def bfs(start):
        queue = deque([(start[0], start[1], 0)])  # (x, y, time)
        visited = set()
        visited.add((start[0], start[1]))
        fruits_collected = 0
        
        while queue:
            x, y, time = queue.popleft()
            if time > time_limit:
                break
            fruits_collected += grid[x][y]
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, time + 1))
        
        return fruits_collected
    
    # 친구들이 시작 위치에서 BFS 탐색을 하고 결과를 저장합니다.
    initial_fruits = [bfs(start) for start in start_positions]
    
    # 친구들이 이동하면서 얻는 최대 열매 수확량을 합산합니다.
    max_fruits = sum(initial_fruits)
    
    return max_fruits

# 입력 처리
n, m = map(int, input().strip().split())
grid = [list(map(int, input().strip().split())) for _ in range(n)]
start_positions = [tuple(map(lambda x: int(x) - 1, input().strip().split())) for _ in range(m)]

# 3초 동안 최대로 얻을 수 있는 열매 수확량의 총 합을 계산합니다.
result = bfs_max_fruits(grid, start_positions, 3)

print(result)
