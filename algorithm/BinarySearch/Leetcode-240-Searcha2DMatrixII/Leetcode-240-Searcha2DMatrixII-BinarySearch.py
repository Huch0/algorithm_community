import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for line in matrix :
            index = bisect.bisect_left(line,target)
            if index < len(line) and line[index] == target :
                return True
        return False