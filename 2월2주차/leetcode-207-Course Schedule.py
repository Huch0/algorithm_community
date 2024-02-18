# 방향 그래프에서 사이클 유무를 판단하려면 연결되어있는 모든 edge들을 통해 다른 node들에 방문해 줘야함
# 따라서 시간복잡도는 v(v+e), n^2의 시간 복잡도를 가짐
# 그런데 최적화(가지치기)를 하니까 시간 복잡도가 엄청엄청 많이 내려갔음
# 최적화가 그만큼 중요한 듯

class Solution: # n^2의 시간 복잡도를 가지는 풀이
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqdict = {}
        for i in range(numCourses):
            reqdict[i] = set()
        for prereq in prerequisites:
            reqdict[prereq[0]].add(prereq[1])

        for i in range(numCourses):
            for j in range(numCourses):
                if i in reqdict[j]:
                    reqdict[j] = reqdict[i] | reqdict[j]

        for i in range(numCourses):
            if i in reqdict[i]:
                return False
        return True

class Solution: # dfs - 그래프가 순환 구조인지 판단 / 앞의 내 풀이가 더 빠름
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqdict = collections.defaultdict(list)
        for req in prerequisites:
            reqdict[req[0]].append(req[1])

        tracing = [0]*numCourses
        def iscycle(i):
            if tracing[i]:
                return True

            tracing[i] = 1
            for node in reqdict[i]:
                if iscycle(node):
                    return True
            tracing[i] = 0
            return False

        for course in list(reqdict):
            if iscycle(course):
                return False
        return True

class Solution: # 앞의 dfs 풀이, 가지치기를 이용해 최적화
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        def dfs(i): # cycle이 있으면 false, 없으면 true 리턴
            if visited[i] == -1:
                return True
            elif visited[i] == 1:
                return False

            visited[i] = 1
            for y in graph[i]:
                if not dfs(y):
                    return False
            visited[i] = -1
            return True

        for x in list(graph):
            visited = [0]*numCourses # 한번도 방문 안했으면 0, dfs 수행 중이면 1, dfs가 종료되었으면 -1. -> -1이면 더이상 볼필요 x
            if not dfs(x):
                return False
        return True