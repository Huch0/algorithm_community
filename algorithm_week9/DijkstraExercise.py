INF = int(1e9) # 국룰 무한대값
 
# 노드, 엣지 개수 입력
n,m = map(int, input().split())
# 시작 노드 번호 입력
start = int(input())
# 그래프 정보 리스트
graph = [[] for i in range(n+1)]
# 방문 여부 리스트
visited = [False]*(n+1)
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF]*(n+1)
 
# 모든 엣지 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    # a -> b 비용은 c이다!
    graph[a].append((b,c))
 
# 방문하지 않은 노드 중에서 가장 최단거리가 짧은 노드의 번호 리턴!!! (핵심)
def get_smallest_node():
    min_value=INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index=i
    return index
 
def dijkstra(start):
    #시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    #시작 노드를 제외한 전체 n-1개의 노드에 대한 반복
    for i in range(n-1):
        #현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True
        #현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost
 
dijkstra(start)
 
#모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    #도달할 수 없는 경우, fail 출력
    if distance[i]==INF:
        print("fail")
    #도달할 수 있는 경우 거리 출력
    else:
        print(distance[i])