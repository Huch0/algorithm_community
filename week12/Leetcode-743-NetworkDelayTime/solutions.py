class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        start = [(0,k)]
        dist = collections.defaultdict(int)

        while start:
            time, node = heapq.heappop(start)
            if node not in dist:
                dist[node] = time
                for neighbor, time2 in graph[node]:
                    alt = time + time2
                    heapq.heappush(start, (alt, neighbor))
        
        if len(dist) == n:
            return max(dist.values())
        return -1
