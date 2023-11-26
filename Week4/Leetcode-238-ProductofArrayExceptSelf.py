class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        left_product = 1

        for i in range(len(nums)):
            results.append(left_product)
            left_product *= nums[i]
        
        right_product = 1
        
        for i in range(len(nums)-1,0-1,-1):
            results[i] *= right_product
            right_product *= nums[i]
        
        return results
    
""" 
Time complexity O(n) solution
    class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        left_product = 1

        for i in range(len(nums)):
            results.append(left_product)
            left_product *= nums[i]
        
        right_product = 1
        for i in range(len(nums)-1,0-1,-1):
            results[i] *= right_product
            right_product *= nums[i]
        
        return results
"""