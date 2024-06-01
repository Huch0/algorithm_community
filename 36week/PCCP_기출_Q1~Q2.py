def solution1(bandage, health, attacks):
    t, x, y = bandage
    time = 0
    max_h = health
    for i in range(len(attacks)):
        at, d = attacks[i]
        health += ((at - time - 1) // t ) * y + (at - time - 1) * x
        if health > max_h:
            health = max_h
        health -= d
        time = at
        if health <= 0:
            return -1
    return health

from collections import deque

def bfs(col, land):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    result = 0
    queue = deque()
    visited = [[False for _ in range(len(land[0]))] for _ in range(len(land))]
    
    for i in range(len(land)):
        if visited[i][col] or land[i][col] == 0:
            continue
        queue.append((i, col))
        visited[i][col] = True
        count = 1
        #print(queue[0], end = " ")
        
        while queue:
            cur_x, cur_y = queue.popleft()
            if land[cur_x][cur_y] == 0:
                break
            for dir in range(4):
                nx, ny = cur_x + dx[dir], cur_y + dy[dir]
                
                if nx < 0 or nx >= len(land) or ny < 0 or ny >= len(land[0]):
                    continue
                    
                if visited[nx][ny] or land[nx][ny] == 0:
                    continue
                
                visited[nx][ny] = True
                count += 1
                queue.append((nx, ny))
        
        result += count
        #print(result)
    return result

def solution2(land):
    answer = 0
    for i in range(len(land[0])):
        count = bfs(i, land)
        if answer < count:
            answer = count
    return answer
