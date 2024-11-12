class Solution:
    def search(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            return -1

'''
#intended solution

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, nums.length - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Determine which half is sorted
            if nums[left] <= nums[mid]:  # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target is in the left half
                else:
                    left = mid + 1   # Target is in the right half
            else:  # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Target is in the right half
                else:
                    right = mid - 1  # Target is in the left half
        
        return -1  # Target not found
'''