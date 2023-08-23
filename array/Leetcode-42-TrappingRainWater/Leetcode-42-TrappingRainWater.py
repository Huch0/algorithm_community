class Solution(object):
    def trap(self, height):
        trappedWater = 0
        while(max(height) > 0):
            topLine = []
            for i in range(len(height)):
                if height[i] == max(height):
                    topLine.append(i)
                    height[i] -= 1
                
            if len(topLine) >= 2:
                trappedWater += (max(topLine) - min(topLine) - len(topLine) + 1)
            
        return trappedWater
#time limit exceeded

# class Solution(object):
#     def trap(self, height):
#         if not height:
#             return 0
        
#         volume = 0
#         left, right = 0, len(height) - 1
#         left_max, right_max = height[left], height[right]

#         while left < right:
#             left_max, right_max = max(height[left], left_max), max(height[right], right_max)
#             if left_max <= right_max:
#                 volume += left_max - height[left]
#                 left += 1
#             else:
#                 volume += right_max - height[right]
#                 right -= 1
            
#         return volume

# class Solution(object):
#     def trap(self, height):
#         stack = []
#         volume = 0

#         for i in range(len(height)):
#             while stack and height[i] > height[stack[-1]]:
#                 top = stack.pop

#                 if not len(stack):
#                     break

#                 distance = i - stack[-1] - 1
#                 waters = min(height[i], height[stack[-1]]) - height[top]

#                 volume += distance * waters

#             stack.append(i)
#         return volume