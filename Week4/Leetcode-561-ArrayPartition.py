class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        num_sum = 0
        for i in range(0,len(nums),2) :
            num_sum += nums[i]
        
        return num_sum
    
"""
another solution

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        num_sum = 0

        for i in range(0,len(nums),2):
            num_sum += min(nums[i],nums[i+1])    
        
        return num_sum
"""