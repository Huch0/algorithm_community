class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        center = 0
        right = len(nums)
        pivot = 1

        while center < right:
            if nums[center] > pivot:
                right -= 1
                nums[right], nums[center] = nums[center], nums[right]
            elif nums[center] < pivot:
                nums[center], nums[left] = nums[left], nums[center]
                center += 1
                left += 1
            else:
                center += 1
        return
