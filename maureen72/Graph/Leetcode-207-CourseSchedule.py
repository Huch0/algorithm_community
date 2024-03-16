class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        adj = collections.defaultdict(list)
        indeg = [0] * numCourses

        for course, pre in prerequisites:
            indeg[course] += 1
            adj[pre].append(course)

        queue = collections.deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                queue.append(i)

        visited = 0
        while queue:
            cur_node = queue.popleft()
            visited += 1
            for neighbor in adj[cur_node]:
                indeg[neighbor] -= 1
                if indeg[neighbor] == 0:
                    queue.append(neighbor)

        return numCourses == visited