class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        for row in matrix:
            l, h = 0, cols - 1
            while l <= h:
                m = (l + h) // 2
                if row[m] == target:
                    return True
                if row[m] < target:
                    l = m + 1
                else:
                    h = m - 1
        return False
