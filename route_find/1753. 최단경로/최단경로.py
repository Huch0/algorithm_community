import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

def dijkstra(start):
    distances = [INF] * (V + 1)  # 최단 거리 테이블을 모두 무한으로 초기화
    distances[start] = 0  # 시작 노드에 대해서 거리를 0으로 설정
    queue = []
    heapq.heappush(queue, (0, start))  # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입

    while queue:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        current_distance, current_node = heapq.heappop(queue)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distances[current_node] < current_distance:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for adjacent, weight in graph[current_node]:
            distance = current_distance + weight
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))

    return distances

# 노드의 개수, 간선의 개수를 입력받기
V, E = map(int, input().split())

# 시작 노드 번호를 입력받기
K = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(V + 1)]

# 모든 간선 정보를 입력받기
for _ in range(E):
    u, v, w = map(int, input().split())
    # u번 노드에서 v번 노드로 가는 비용이 w라는 의미
    graph[u].append((v, w))

# 다익스트라 알고리즘을 수행
result = dijkstra(K)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, V + 1):
    # 도달할 수 없는 경우, INF 출력
    if result[i] == INF:
        print("INF")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(result[i])