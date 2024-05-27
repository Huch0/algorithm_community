import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points :
            x,y = point[0], point[1]
            distance_squared = x**2 + y**2
            heapq.heappush(heap,(distance_squared,[x,y]))
        
        result = []
        for _ in range(k) :
            result.append(heapq.heappop(heap)[1])
        return result