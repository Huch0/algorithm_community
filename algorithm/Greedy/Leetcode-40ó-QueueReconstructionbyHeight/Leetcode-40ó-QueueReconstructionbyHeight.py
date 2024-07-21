import heapq

class Solution :
    def reconstructQueue(self , people: list[list[int]] ) -> list[list[int]] :
        heap = []
        result = []
        
        for person in people :
            heapq.heappush(heap,(-person[0],person[1]))
        
        while heap :
            pop = heapq.heappop(heap)
            result.insert(pop[1],(-pop[0],pop[1]))
        
        return result
        
print(Solution.reconstructQueue(Solution,[[7,0] ,[4,4], [7,1], [5,0], [6,1], [5,2]]))