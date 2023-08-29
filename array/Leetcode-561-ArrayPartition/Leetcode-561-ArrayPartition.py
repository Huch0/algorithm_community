class Solution(object):
    def arrayPairSum(self, nums):
        sum = 0
        nums.sort()

        for i in range(0, len(nums), 2):
            sum += nums[i]
        
        return sum

# class Solution(object):
#     def arrayPairSum(self, nums):
#         return sum(sorted(nums)[::2])