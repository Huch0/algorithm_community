class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def distance(point):
            return point[0] ** 2 + point[1] ** 2
        
        points.sort(key=distance)

        return points[:k]