import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1] : 
                start = i+1
                break

        left = start
        right = len(nums)
        
        result = bisect.bisect_left(nums,target,left,right)
        if result < len(nums) and nums[result] == target :
            return result
        
        left = 0
        right = start
        result = bisect.bisect_left(nums,target,left,right)
        if result < right and nums[result] == target :
            return result
        
        return -1