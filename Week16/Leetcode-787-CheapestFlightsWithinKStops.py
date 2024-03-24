class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for start, destination, weight in flights :
            graph[start].append([destination,weight])
        
        Q = collections.deque([[0,src]])

        arrive = collections.defaultdict(int)

        level = 0

        q_previous = 1
        q_in = 0
        q_out = 0

        while level <= k+1:
            while q_out < q_previous :
                cost, stop = Q.popleft()
                q_out += 1

                if stop not in arrive or arrive[stop] > cost:
                    arrive[stop] = cost
                    for destination, weight in graph[stop] :
                        Q.append((cost+weight,destination))
                        q_in += 1
            
            q_previous = q_in
            q_in = 0
            q_out = 0
            level += 1
        
        if dst in arrive : return arrive[dst]
        else : return -1
            
            
