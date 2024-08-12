# 처음에는 그래프 모든 노드에 대해 다익스트라를 돌려서, 모든 노드가 root였을 때의 height를 전부 구하려고 했다.
# 시간 초과가 떠서 좀 더 생각해 봤더니, 다익스트라보다 bfs로 높이를 세는게 더 빠를 것 같았지만 이것도 시간 초과가 떴다
# 풀이 방향을 잘 잡는게 중요하다.. 근데 이걸 솔루션 안보고 떠올리는게 가능한가 ? ...

import copy as cp
class Solution: # 모든 노드에 대해 bfs 돌리기 (시간 초과)
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def getheight(n, connection):
            connection = cp.deepcopy(connection)
            height = 0
            dq = collections.deque([n])
            while dq:
                height = height + 1
                for i in range(len(dq)):
                    cur = dq.popleft()
                    for node in connection[cur]:
                        dq.append(node)
                        connection[node].remove(cur)
            return height

        graph = collections.defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        heights = [0 for x in range(n)]
        for i in range(n):
            heights[i] = getheight(i, graph)

        answer = []
        minimum = min(heights)
        for i in range(n):
            if heights[i] == minimum:
                answer.append(i)
        return answer
    
class Solution: # 솔루션 보고 작성한 답안. 근데 또 너무 느림 (3000ms)
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {}
        for i in range(n):
            graph[i] = []
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        while len(graph) > 2:
            todel = [] # (a,b)의 tuple형식으로 저장
            for key, value in graph.items():
                if len(value) == 1:
                    todel.append(key)
            for leaf in todel:
                graph[graph[leaf][0]].remove(leaf)
                del graph[leaf] # dictionary에서 특정 key를 delete하는건 보통 o(1)만에 가능하다

        answer = []
        for key in graph.keys():
            answer.append(key)
        return answer

# 솔루션 참고해서 작성
# leaf를 뗴어낸 다음에 다음 leaf를 찾을 때 필요한 것만 찾는다는게 포인트였음
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
            
        graph = collections.defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        leaves = []
        for key, value in graph.items():
            if len(value) == 1:
                leaves.append(key)

        while n > 2:
            newleaves = []
            n = n - len(leaves)
            for leaf in leaves:
                connectednode = graph[leaf].pop()
                graph[connectednode].remove(leaf)
                if len(graph[connectednode]) == 1:
                    newleaves.append(connectednode)
            leaves = newleaves

        return leaves
        