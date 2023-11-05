class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:      
        def backtracking(path, remaining_nums):
            if not remaining_nums:
                result.append(path)
                return
            for i in range(len(remaining_nums)):
                backtracking(path + [remaining_nums[i]], remaining_nums[:i] + remaining_nums[i+1:])

        result = []
        backtracking([], nums)
        return result