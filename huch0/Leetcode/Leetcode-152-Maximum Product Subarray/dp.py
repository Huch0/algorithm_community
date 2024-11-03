class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        global_max = cur_max = cur_min = nums[0]

        for i in range(1, n):
            candidate = (nums[i], cur_max * nums[i], cur_min * nums[i])
            cur_max = max(candidate)
            cur_min = min(candidate)

            global_max = max(global_max, cur_max)

        return global_max
