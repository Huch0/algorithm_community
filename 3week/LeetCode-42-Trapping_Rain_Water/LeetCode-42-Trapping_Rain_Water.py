def count_water(target: int, min_height: int, heights: list[int]) -> int:

    result = 0

    for i, height in enumerate(heights):
        if height >= target:
            return 0
        else:
            continue

    return result
            
        

class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) == 1:
            return 0
        
        result = 0

        max_height = max(height)
        min_height = 0
        target = min(num for num in height if num != min_height)
        
        while target != max_height:
            result += count_water(target, min_height, height)

            min_height = target
            height = [num for num in height if num <= min_height]
            target = min(num for num in height if num != min_height)

        return result
        
