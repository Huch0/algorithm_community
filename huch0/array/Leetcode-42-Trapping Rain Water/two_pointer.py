class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        
        # Use Two pointer Algorithm
        left, right = 0, len(height) - 1
        # (left_max, right_max) is sub array for a puddle.
        left_max, right_max = left, right

        while left < right:
            if height[left_max] <= height[right_max]:
                volume += height[left_max] - height[left]
                left += 1
                if height[left] > height[left_max]:
                    left_max = left
            else:
                volume += height[right_max] - height[right]
                right -= 1
                if height[right] > height[right_max]:
                    right_max = right
            
        
        return volume