class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        Sum = [nums[0]]
        for i in range(1,len(nums)) :
            if Sum[i-1] < 0 : Sum.append(nums[i])
            else : Sum.append(Sum[i-1]+nums[i])
        return max(Sum)