class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        for x, y in prerequisites:
            graph[x].append(y)

        frontier = set()
        visited = set()

        def dfs(node):
            if node in frontier:
                return False
            if node in visited:
                return True

            frontier.add(node)
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            frontier.remove(node)
            visited.add(node)
            return True
        
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return False
                
        return True
    
# Path: week12/Leetcode-210-course_schedule_ii/solutions.py