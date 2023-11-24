class Solution:
    def __init__(self) -> None:
        self.graph = []
        self.distance = []
        self.visited = []
        self.INF = 999999999
    
    
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        self.graph = [[self.INF] * n for _ in range(n)]
        self.visited = [False] * n

        for u, v, w in times:
            self.graph[u - 1][v - 1] = w

        for i in range(n):
            self.graph[i][i] = 0
        
        def get_small_index():
            min = self.INF
            index = 0
            for i in range(len(self.distance)):
                if self.distance[i] < min and self.visited[i] == False:
                    min = self.distance[i]
                    index = i
            return index
        
        def dijkstra(start):
            self.distance = self.graph[start]
            self.visited[start] = True

            for i in range(n - 2):
                current = get_small_index()
                self.visited[current] = True
                for j in range(n):
                    if self.visited[j] == False:
                        if self.distance[current] + self.graph[current][j] < self.distance[j]:
                            self.distance[j] = self.distance[current] + self.graph[current][j]

            self.visited = [False] * n

        dijkstra(k - 1)
        if self.INF in self.distance:
            return -1
        else:
            return max(self.distance)