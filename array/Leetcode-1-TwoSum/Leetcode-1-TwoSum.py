class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# class Solution(object):
#     def twoSum(self, nums, target):
#         for i, n in enumerate(nums):
#             complement = target - nums
            
#             if complement in nums[i + 1]:
#                 return [nums.index(n), nums[i+1:].index(complement) + (i + 1)]

# class Solution(object):
#     def twoSum(self, nums, target):
#         nums_map = {}
#         for i, num in enumerate(nums):
#             if target - num in nums_map:
#                 return [nums_map[target - num], i]
#             nums_map[num] = i

# class Solution(object):
#     def twoSum(self, nums, target):
#         left, right = 0, len(nums) - 1
#         while not left == right:
#             if nums[left] + nums[right] < target:
#                 left += 1
#             elif nums[left] + nums[right] > target:
#                 right -= 1
#             else:
#                 return [left, right]
# not sorted