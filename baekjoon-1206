from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for node in graph:
    node.sort(reverse=True)
    
visited = [-1] * (N+1)
stack = [V]
while stack:
    node = stack.pop()
    if visited[node] == -1:
        visited[node] = 1
        print(node, end=" ")
        for next_node in graph[node]:
            stack.append(next_node)

print()

for node in graph:
    node.sort()
    
visited = [-1] * (N+1)
q = deque()
q.append(V)
while q:
    node = q.popleft()
    if visited[node] == -1:
        visited[node] = 1
        print(node, end=" ")
        for next_node in graph[node]:
            q.append(next_node)
