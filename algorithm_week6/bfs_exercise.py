from collections import deque # bfs는 deque를 이용한다.

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True # 첫 노드 방문처리
    while queue: # python에서 빈 자료구조는 'False'로 평가되기 때문에, 아무것도 남아있지 않을 때까지 반복한다는 뜻.
        v = queue.popleft() # 맨 앞 노드를 방문 하면서
        print(v, end = ' ')
        for i in graph[v]: # 방문한 노드의 인접 노드들을 살펴봄. v의 모든 인접노드들을 방문.
            if not visited[i]: # 방문 안 한 노드가 있으면
                queue.append(i) # 그 노드를 큐의 뒤에 집어넣고
                visited[i] = True # 방문처리.

bfs(graph, 1, visited)

