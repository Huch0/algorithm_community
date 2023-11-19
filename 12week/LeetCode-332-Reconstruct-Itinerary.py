import collections

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        routes = []

        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop())
            routes.append(a)
        
        dfs('JFK')
        return routes[::-1]