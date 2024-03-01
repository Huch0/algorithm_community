class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        dist = []
        for i in range(len(points)):
            tmp_dist = points[i][0] ** 2 + points[i][1]**2
            dist.append((tmp_dist, points[i]))
        
        sorted_dist = sorted(dist)
        print(sorted_dist)
            
        for j in range(k):
            ans.append(sorted_dist[j][1])
        
        return ans
