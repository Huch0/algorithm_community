class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        i, j = 0, 0

        while i < rows:
            # Search the row
            while j < cols:
                if matrix[i][j] == target:
                    return True

                if matrix[i][j] > target:
                    break

                j += 1
            # Search the column
            j -= 1  # No need to search jth column again
            i += 1  # No need to search ith row again
            while i < rows:
                if matrix[i][j] == target:
                    return True

                if matrix[i][j] > target:
                    break

                i += 1

            j = 0  # Reset j to 0 to search the next row

        return False
