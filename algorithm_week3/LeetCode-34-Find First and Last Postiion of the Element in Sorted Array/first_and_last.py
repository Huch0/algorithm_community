class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def find_start(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def find_end(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        start = find_start(nums, target)
        end = find_end(nums, target)
        
        if start > end:
            return [-1, -1]
        
        return [start, end]

