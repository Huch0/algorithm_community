class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Sort nums
        nums.sort()
        sum_of_mins = 0

        # Add numbers which indices are even.
        for i in range(0, len(nums), 2):
            sum_of_mins += nums[i]
        
        return sum_of_mins