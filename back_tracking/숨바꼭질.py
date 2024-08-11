from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
dist = [-1] * (N+1)

# 그래프 생성
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)


q = deque([1])
dist[1] = 0

while q:
    cur = q.popleft()
    for node in graph[cur]:
        if dist[node] == -1:
            q.append(node)
            dist[node] = dist[cur] + 1

max_dist = max(dist)
furthest_barns = [i for i, d in enumerate(dist) if d == max_dist]

furthest_barn = min(furthest_barns)
num_furthest = len(furthest_barns)
print(furthest_barn, max_dist, num_furthest)
