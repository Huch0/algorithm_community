class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def is_loop(node: int) -> bool:
            # Return True if node is already in traced
            if node in traced:
                return True

            # Return False if node is already in studied
            # for pruning
            if node in studied:
                return False

            traced.add(node)

            for next_node in graph[node]:
                if is_loop(next_node):
                    return True
                # if is_loop(next_node) is False, don't need to return

            # Remove node from traced after trace all possible path
            traced.remove(node)

            # Add node to studied
            studied.add(node)

            return False

        # For check if node is traced in one path
        traced = set()
        # For check if node is studied in whole path, for pruning
        studied = set()

        graph = collections.defaultdict(list)

        for arrival, departure in prerequisites:
            graph[departure].append(arrival)

        for node in list(graph):
            if is_loop(node):
                return False

        return True
