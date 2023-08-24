class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        product = 1

        # Get product of left side of each element
        for i in range(len(nums)):
            products.append(product)
            product *= nums[i]
        
        # Get product of right side of each element
        product = 1
        for i in range(len(nums) - 1, 0 - 1, -1):
            products[i] *= product
            product *= nums[i]
        
        return products

