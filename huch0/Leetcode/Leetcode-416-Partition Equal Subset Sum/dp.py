class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp, s = set([0]), sum(nums)
        if s&1:
            return False
        for num in nums:
            dp.update([v+num for v in dp if v+num <= s>>1])
        return s>>1 in dp