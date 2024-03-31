class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = cur_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum = max(nums[i], cur_sum + nums[i])
            best_sum = max(best_sum, cur_sum)
        return best_sum
