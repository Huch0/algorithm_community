import sys

def bellman_ford(n, edges, start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0

    for i in range(n):
        for cur, next_node, cost in edges:
            if dist[cur] != float('inf') and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                if i == n - 1:  # 음수 사이클 감지
                    return None

    return dist[1:]

# 입력 받기
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# 벨만-포드 알고리즘 실행
result = bellman_ford(n, edges, 1)

# 결과 출력
if result is None:
    print(-1)
else:
    for dist in result[1:]:
        print(dist if dist != float('inf') else -1)