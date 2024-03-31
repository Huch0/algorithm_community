class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Multiply all elements in nums
        product_of_nums = 1

        for num in nums:
            product_of_nums *= num

        results = []
        for i in range(len(nums)):
            # if nums[i] == 0, should obtain product again.
            # because product_of_nums would be 0.
            if nums[i] == 0:
                product = 1
                for j in range(len(nums)):
                    if j != i:
                        product *= nums[j]
                results.append(product)
            else:
                # Divide product_of_nums by num[i]. 
                # (a * b * c * ... // a) == (b * c * ...)
                results.append(product_of_nums // nums[i])


        return results