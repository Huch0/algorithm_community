class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        count_zero = nums.count(0)
        output = []

        if count_zero > 1:
            return [0] * len(nums)
        elif count_zero == 1:
            product = 1
            for num in nums:
                if num != 0:
                    product = product * num
            output = [0] * len(nums)
            output[nums.index(0)] = product
        else:
            product = 1
            for num in nums:
                product = product * num
            output = [product / num for num in nums]

        return output
