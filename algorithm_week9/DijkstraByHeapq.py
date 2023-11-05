import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
 
n,m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)
 
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
 
def dijkstra(start):
    q=[]
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    # q가 비어있지 않다면
    while q:
        # 가장 최단 거리인 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리됐다면 skip
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거치면 이동 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
 
dijkstra(start)
 
#모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    #도달할 수 없는 경우, fail 출력
    if distance[i]==INF:
        print("fail")
    else:
        print(distance[i])