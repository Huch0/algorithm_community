class Solution(object):
    def permute(self, nums):
        result = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            elements = self.permute(nums)

            for e in elements:
                e.append(n)
                result.append(e)

            nums.append(n)

        return result