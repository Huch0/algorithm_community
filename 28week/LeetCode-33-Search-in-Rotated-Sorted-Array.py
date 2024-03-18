class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        jump = right // 2

        while jump >= 1:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if nums[right-jump] == target:
                return right-jump
            
            if nums[left+jump] < target and nums[left] < nums[left+jump]:
                left += jump
            elif nums[left+jump] > target and nums[right] > nums[right-jump]:
                right -= jump

            else:
                if abs(nums[left]-target) < abs(nums[right]-target):
                    right -= jump
                else:
                    left += jump

            print(left, " ", right, " ",jump)

            jump = (right-left) // 2
        
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1
