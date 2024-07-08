class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Flat matrix into 1D list.
        # flatten = [elem for row in matrix for elem in row]
        # m = bisect.bisect_left(flatten, target)
        # return True if 0 <= m < len(flatten) and flatten[m] == target else False

        # Index trick
        M, N = len(matrix), len(matrix[0])
        l, h = 0, M * N - 1
        while l <= h:
            m = (l + h) // 2
            i, j = m // N, m % N
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                l = m + 1
            else:
                h = m - 1

        return False
