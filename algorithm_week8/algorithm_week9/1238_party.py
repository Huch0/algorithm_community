import heapq

InumNodeF = int(1e9)

def dijkstra(graph, start, n):
    distance = [InumNodeF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
    return distance

numNode, numEdge, party = map(int, input().split())

graph = [[] for _ in range(numNode + 1)]
reverse_graph = [[] for _ in range(numNode + 1)]

for _ in range(numEdge):
    start, end, time = map(int, input().split())
    graph[start].append((end, time))
    reverse_graph[end].append((start, time))

to_party = dijkstra(graph, party, numNode)

from_party = dijkstra(reverse_graph, party, numNode)

maparty_time = 0
for i in range(1, numNode + 1):
    maparty_time = max(maparty_time, to_party[i] + from_party[i])

print(maparty_time)
