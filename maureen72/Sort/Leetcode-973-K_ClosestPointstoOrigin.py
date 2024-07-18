class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        lst = []
        for (x,y) in points:
            distance = x**2 + y**2
            lst.append((distance, x, y))
        lst.sort()
        return [[x, y] for (_, x, y) in lst[:k]]

        