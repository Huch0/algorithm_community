class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = collections.defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v,w))
        
        Q = [(0,src,k)]

        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k>=0:
                for v,w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k-1))
        
        return -1