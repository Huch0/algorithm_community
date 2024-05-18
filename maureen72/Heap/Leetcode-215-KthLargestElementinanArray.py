class Solution(object):
    def findKthLargest(self, nums, k):
        sorted_nums = sorted(nums, reverse = True)
        return sorted_nums[k-1]