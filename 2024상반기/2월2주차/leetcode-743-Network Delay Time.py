# 힙은 최댓값/최솟값을 찾아내는 연산을 빠르게 하기 위해 고안된, 완전이진트리를 기본으로 한 자료구조이다.
# 완전이진트리란, 가장 아래 레벨을 제외한 모든 레벨에서 모든 노드들이 채워진 트리를 말한다.
# 힙의 부모와 자식 노드 간에는 대소 관계가 존재한다.
# 요소의 삽입과 삭제(루트노드)는 (logn), 요소 탐색은 (n)시간이 걸린다

class Solution: # 처음 풀이
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
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

# 다익스트라 알고리즘에서 특정 노드에 방문하여 그 노드에서 bfs를 수행한다는 것은, 그 노드까지의 거리는 최단거리라는 전제 하에 수행하는 것이다
# 아래 알고리즘을 보면 노드에 처음 방문했을 때만 dist를 업데이트하는데, 그 다음부터는 그 노드에 방문하더라도 처음 거리보다 길기 때문이다.
# 이떄 음수 간선이 있으면 이 전제가 깨지기 때문에, 음수 간선이 있으면 다익스트라를 사용할 수 없다.
class Solution: # 다음 방문 노드 찾을 때 pq이용해서 최적화
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