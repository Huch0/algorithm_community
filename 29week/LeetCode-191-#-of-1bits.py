class Solution:
    def hammingWeight(self, n: int) -> int:
        masks = [0x1, 0x3, 0xF, 0xFF, 0xFFFF]
        
        def count_1bit(nums, height):
            if height < 0:
                return nums
            count = 0
            left = (nums & (masks[height] << (2**height))) >> (2**height)
            if left:
                count += count_1bit(left, height - 1)
            right = nums & masks[height]
            if right:
                count += count_1bit(right, height - 1)
            return count
        
        return count_1bit(n, 4)