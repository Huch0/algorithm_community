# priority queue 없이 풀기
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int: # pq 사용법 ?
        graph = collections.defaultdict(list)
        for edge in times:
            graph[edge[0]].append((edge[1], edge[2]))
        time = [999999 for _ in range(n+1)]
        time[k] = 0
        unvisited = [x for x in range(1, n+1)]
        unvisited = set(unvisited)

        # 다익스트라 알고리즘 돌려서 time 갱신
        while unvisited:
            m = 999999
            nextnode = 0
            for i in unvisited:
                if time[i] < m:
                    m = time[i]
                    nextnode = i
            if nextnode == 0:
                break
            unvisited.remove(nextnode) #nextnode 방문
            for edge in graph[nextnode]:
                if time[edge[0]] > edge[1] + time[nextnode]:
                    time[edge[0]] = edge[1] + time[nextnode]

        #time을 활용해서 답 내기
        time[0] = 0
        answer = max(time)
        if answer == 999999:
            return -1
        else:
            return answer
        
# pq로 개선된 풀이
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        myheap = [(0, k)]
        delayDict = collections.defaultdict(int)
        while myheap:
            time, node = heapq.heappop(myheap)
            if node not in delayDict:
                delayDict[node] = time
                for nextnode, delay in graph[node]:
                    heapq.heappush(myheap, (time+delay, nextnode))

        if len(delayDict) != n:
            return -1
        else:
            M = 0
            for t in delayDict.values():
                if M < t:
                    M = t
            return M