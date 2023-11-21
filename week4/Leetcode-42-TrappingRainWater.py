class Solution(object):
    def trap(self, height):

        rain = 0
        # Two pointer Algorithm
        left = 0
        right = len(height) - 1

        left_max, right_max = height[left], height[right]

        while left < right:

            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)
            if left_max <= right_max:
                rain += left_max - height[left]
                left += 1
            else:
                rain += right_max - height[right]
                right -= 1
            
        
        return rain