class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return nums[0]

        l = self.majorityElement(nums[:n // 2])
        r = self.majorityElement(nums[n // 2:])

        if nums.count(l) > n // 2:
            return l
        return r
