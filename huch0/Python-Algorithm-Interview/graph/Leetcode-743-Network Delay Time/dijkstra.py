class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = sys.maxsize

        # Initate distances
        # index 0 isn't be used.
        # start node's distance is 0
        distances = [INF] * (n + 1)
        distances[k] = 0

        visited = [k]
        current_node = k

        i = 1

        while i < n:
            # Set adjacent nodes' distance
            for time in times:
                if time[0] == current_node:
                    # Select lower distance between previous distance and distance to current_node + weight
                    distances[time[1]] = min(
                        distances[time[1]], distances[current_node] + time[2])

            # Set closest node as current_node
            # which is not in visited
            min_distance_node = 0

            for node in range(1, n + 1):
                if node not in visited:
                    if distances[node] < distances[min_distance_node]:
                        min_distance_node = node

            current_node = min_distance_node

            # current_node == 0, it means
            # All possible node (connected with other) is visited.
            # There are some nodes that are not connected with others
            # So, It is impossible for all the n nodes to receive the signal
            if current_node == 0:
                return -1

            visited.append(current_node)

            i += 1

        # Furthest node is last node
        return max(distances[1:])
