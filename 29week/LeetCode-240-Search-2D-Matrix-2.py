class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
       
        for row in matrix:
            if row[0] <= target <= row[-1]:
                l, r = 0, n-1
                while l <= r:
                    mid = (l + r) // 2
                    if target == row[mid]:
                        return True
                    elif target > row[mid]:
                        l = mid + 1
                    else:
                        r = mid - 1
        return False

        # return any(target in row for row in matrix) // It works good space complexity is O(1)


        # left_row, left_col = 0, 0
        # right_row, right_col = m-1, n-1
        # mid = [(left_row + right_row) // 2, (left_col + right_col) // 2]

        # def binary_search_row(l, r, row):
        #     left = l
        #     right = r

        #     mid = (left + right) // 2
        #     nums = matrix[row]

        #     while left <= right:
        #         if target == nums[mid]:
        #             return True
        #         elif target > nums[mid]:
        #             left = mid+1
        #         else:
        #             right = mid-1
        #         mid = (left + right) // 2
        #     return False
        
        # def binary_search_col(l, r, col):
        #     left = l
        #     right = r
        #     mid = (left + right) // 2

        #     while left <= right:
        #         if target == matrix[mid][col]:
        #             return True
        #         elif target > matrix[mid][col]:
        #             left = mid+1
        #         else:
        #             right = mid-1
        #         mid = (left + right) // 2
        #     return False

        # while left_row <= right_row and left_col <= right_col:
            
        #     print(mid)
        #     pivot = matrix[mid[0]][mid[1]]
        #     if target == pivot:
        #         return True
        #     elif target > pivot:
        #         if binary_search_row(mid[1] + 1, n-1, mid[0]) or binary_search_col(mid[0]+1, m-1, mid[1]):
        #             return True
        #         left_row, left_col = mid[0] + 1, mid[1] + 1
        #     else:
        #         if binary_search_row(0, mid[1]-1, mid[0]) or binary_search_col(0, mid[0]-1, mid[1]):
        #             return True
        #         right_row, right_col = mid[0] - 1, mid[1] - 1

        #     ##scailing
        #     if left_row >= m:
        #         left_row = m - 1
        #     if left_col >= n:
        #         left_col = n - 1
        #     if right_row < 0:
        #         right_row = 0
        #     if right_col < 0:
        #         right_col = 0
        #     mid = [(left_row + right_row) // 2, (left_col + right_col) // 2]
        #     if (left_row == m - 1 and left_col == n - 1) or (right_row == 0 and right_col == 0):
        #         break
        # if target == matrix[mid[0]][mid[1]]:
        #     return True

        # print(mid)
        # return False

        # def negetive_to_zero(a):
        #     if a > 0:
        #         return 1
        #     else:
        #         return 0

        # for i in range(diff):
        #     left, right = 0, min(m, n) - 1 
        #     while left <= right:
        #         mid = (left + right) // 2
        #         row = mid + i * negetive_to_zero(m-n)
        #         col = mid + i * negetive_to_zero(n-m)
        #         pivot = matrix[row][col]
        #         print(row, col)
        #         if target == pivot:
        #             return True
        #         elif target > pivot:
        #             if binary_search_row(col + 1, n - 1, row) or binary_search_col(row + 1, m - 1, col):
        #                 return True
        #             left = mid + 1
        #         else:
        #             if binary_search_row(0, col - 1, row) or binary_search_col(0, row - 1, col):
        #                 return True
        #             right = mid - 1