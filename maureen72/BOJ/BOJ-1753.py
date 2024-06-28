import sys
import heapq

INF = float('inf')

class Vertex:
    def __init__(self):
        self.edges = []

def dijkstra(V, adj, start):
    pq = []
    answer = [INF] * (V + 1)
    answer[start] = 0
    heapq.heappush(pq, (0, start))
    
    while pq:
        cost, now = heapq.heappop(pq)
        if answer[now] < cost:
            continue
        for nxt, nxt_cost in adj[now]:
            if answer[nxt] > answer[now] + nxt_cost:
                answer[nxt] = answer[now] + nxt_cost
                heapq.heappush(pq, (answer[nxt], nxt))
    
    for i in range(1, V + 1):
        if answer[i] == INF:
            print("INF")
        else:
            print(answer[i])

def main():
    input = sys.stdin.read
    data = input().split()
    V = int(data[0])
    E = int(data[1])
    K = int(data[2])
    
    adj = [[] for _ in range(V + 1)]
    
    index = 3
    for _ in range(E):
        u = int(data[index])
        v = int(data[index + 1])
        w = int(data[index + 2])
        adj[u].append((v, w))
        index += 3
    
    dijkstra(V, adj, K)

if __name__ == "__main__":
    main()
