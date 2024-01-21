class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        lenOfEdges = len(edges)
        connected_nodes_count = [] * n
        found = 0

        for i in range(n):
            node = connected_nodes_count[edges[i][0]]
            leaves = connected_nodes_count[edges[i][1]]

        while found <= 2:
            found = n
            for j in range(n):
                if connected_nodes_count[j] == 1 and found > 2:
                    connected_nodes_count[j] = 0
                    found -= 1
                    for k in range(n):
                        if edges[k][0] == j or edges[k][1] == j:
                            connected_nodes_count[k] -= 1
                            if connected_nodes_count[k] == 0:
                                found -= 1

        return connected_nodes_count
    