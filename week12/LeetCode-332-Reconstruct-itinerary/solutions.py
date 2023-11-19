from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        route = []
        cur_dept = "JFK"
        
        graph = defaultdict(list)
        for dept, arrive in sorted(tickets, reverse=True): 
            graph[dept].append(arrive)
        
        def dfs(dept):
            while graph[dept]:
                dfs(graph[dept].pop())
            route.append(dept)
        
        dfs(cur_dept)
        
        return route[::-1]
