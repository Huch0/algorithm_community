# 이전 문제에서는 처음 방문하는 노드에 대해서만 인접 노드까지의 거리를 더해 pq에 push해주면 되었다.
# 따라서 pq에 들어가게 되는 원소들도 얼마 되지 않았다.
# 이번 문제에서는 처음 방문하는 노드(최단 거리임이 확정된 노드)가 아니더라도 pq에 push해줘야 한다. 최단거리가 아니지만 경유지 수가 작아서 답이 될 수 있기 때문
# 그런데 이렇게 하니까 pq에 너무 많은 원소들이 들어가게 되어서 시간 초과가 났다.
# while문을 돌다가 도착지에 도착하면 즉시 종료하게 프로그램했더니 통과했다. (맨 먼저 도착한게 무조건 최단경로이기 때문)

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for fr, to, price in flights:
            graph[fr].append((to, price))
        
        distance = [(-1, 0) for _ in range(n)]
        pq = [(0, src, -1)] # 가격, 목적지, 경유횟수
        
        while pq:
            d, here, stops = heapq.heappop(pq)
            if here == dst: # 도착하면 바로 종료
                return d
            if distance[here][0] == -1:
                distance[here] = (d, stops)
            if stops < k:
                for path in graph[here]:
                    if distance[path[0]][0] == -1 or distance[path[0]][1] > stops+1: # pq에 최대한 적게 넣으려고 건 조건문
                        heapq.heappush(pq, (d + path[1], path[0], stops+1))

        return distance[dst][0]