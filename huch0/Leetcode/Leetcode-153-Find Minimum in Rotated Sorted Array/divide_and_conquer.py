class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        lmin = self.findMin(nums[:n // 2])
        rmin = self.findMin(nums[n // 2:])

        return min(lmin, rmin)
