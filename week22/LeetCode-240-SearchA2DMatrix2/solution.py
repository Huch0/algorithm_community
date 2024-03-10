class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        
        m = len(mat)
        n = len(mat[0])
        
        for i in range(m):
            if mat[i][0] <= target and mat[i][-1] >= target:
                low = 0
                high=n
                while (low < high):
                    mid = (low + high)//2
                    
                    if mat[i][mid] == target:
                        return True
                    elif mat[i][mid] < target:
                        low = mid + 1
                    else:
                        high = mid
                        
        return False