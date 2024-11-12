import collections

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n <= 1:
            return [0]
        graph = collections.defaultdict(list)

        for i, j in edges:
            graph[i].append(j)  # 무방향 그래프이기 때문에 딕셔너리에 양방향으로 삽입
            graph[j].append(i)

        leaf_nodes = []  # leafnode들 추가
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaf_nodes.append(i)
        while n > 2:
            n -= len(leaf_nodes)
            new_leafNodes = []
            for leaf in leaf_nodes:
                popleaf = graph[leaf].pop()
                graph[popleaf].remove(leaf)

                if len(graph[popleaf]) == 1:
                    new_leafNodes.append(popleaf)  
            leaf_nodes = new_leafNodes  
        return leaf_nodes