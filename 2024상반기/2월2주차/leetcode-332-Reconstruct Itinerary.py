# dfs에서는 가지치기를 통해서 최적화하는게 중요한 것 같음, 이거 때문에 시간 차이가 많이 남

class Solution: # 내 처음 풀이
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        answer = []
        def dfs(current, mytickets, path):
            if len(mytickets) == 0:
                nonlocal answer
                answer = path[:]
                return
            for i in range(0, len(mytickets)):
                if mytickets[i][0] == current:
                    path.append(mytickets[i][1])
                    dfs(mytickets[i][1], mytickets[:i] + mytickets[i+1:], path)
                    if len(answer) != 0:
                        return
                    path.pop()

        path = ["JFK"]
        tickets = sorted(tickets)
        dfs("JFK", tickets, path)
        return answer

class Solution: # 내 최종 풀이
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        answer = []
        def dfs(current, mytickets, path):
            if len(mytickets) == 0:
                nonlocal answer
                answer = path[:]
                return
            
            visited = set()
            for i in range(0, len(mytickets)):
                if mytickets[i][0] == current:
                    if mytickets[i][1] in visited:
                        continue
                    path.append(mytickets[i][1])
                    dfs(mytickets[i][1], mytickets[:i] + mytickets[i+1:], path)
                    if len(answer) != 0:
                        return
                    path.pop()
                    visited.add(mytickets[i][1])

        path = ["JFK"]
        tickets = sorted(tickets)
        dfs("JFK", tickets, path)
        return answer
    
class Solution: # 배열이 아닌 딕셔너리를 이용한 최적화 -> 티켓 찾는 시간이 매우 단축됌
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        numOfTickets = len(tickets)
        answer = []
        def dfs(current, path):
            if len(path) == numOfTickets + 1:
                nonlocal answer
                answer = path[:]
                return

            visited = set()
            for i in range(len(mytickets[current])):
                if mytickets[current][i] in visited:
                    continue
                path.append(mytickets[current][i])
                nextplace = mytickets[current].pop(i)
                dfs(nextplace, path)
                if len(answer) != 0:
                    return
                mytickets[current].insert(i, nextplace)
                path.pop()
                visited.add(nextplace)

        path = ["JFK"]
        mytickets = collections.defaultdict(list)
        for ticket in tickets:
            mytickets[ticket[0]].append(ticket[1])
        for place in mytickets.values():
            place.sort()

        dfs("JFK", path)
        return answer

# 솔루션 - 직관적이지 않아서 이해가 좀 힘들었음ㅡ
# 끊어지는 경로가 없다면 dfs 호출 순서가 곧 방문 순서이다.
# 하지만 끊어지는 경로가 있다면 그곳이 먼저 route에 담기게 되고, 나중에 방문되게 된다.
class Solution: 
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)

        route = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)

        dfs('JFK')
        return route[::-1]
    
# 똑같은 풀이인데 재귀가 아닌 반복으로 풀이
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)

        route = []
        stack = ["JFK"]
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())
        return route[::-1]