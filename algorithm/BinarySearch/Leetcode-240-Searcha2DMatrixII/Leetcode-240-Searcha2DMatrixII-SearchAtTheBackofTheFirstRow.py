class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix : return False 

        row = 0 
        column = len(matrix[0])-1

        while row < len(matrix) and column >= 0 :
            if matrix[row][column] == target : return True
            elif matrix[row][column] > target : 
                column -= 1
            else : 
                row += 1
        return False 