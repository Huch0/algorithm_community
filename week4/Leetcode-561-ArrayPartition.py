class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        #numlst = []
        #numlst.append(nums[::2])
        result = sum(nums[::2])

        return result