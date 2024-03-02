class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph = collections.defaultdict(list)
        for u,v,w in times: # u:start v:destination w: time
            graph[u].append((v,w))
        
        Q = [[0,k]]  #init value: [time,node]
        dist = collections.defaultdict(int)

        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v,w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt,v))
                
        if len(dist) != n:
            return -1
        else:
            return max(dist.values())
        