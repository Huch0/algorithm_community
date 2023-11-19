#brute force algorithm (first commit)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)) :
                if nums[i] + nums[j] == target :
                    return [i,j]
                
"""
Searching using 'in'

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,n in enumerate(nums):
            complement = target - n

            if complement in nums[i+1:]:
                return [i,nums[i+1:].index(complement) + (i+1)]
"""

"""
Solving using dictionary

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for index, num in enumerate(nums):
            nums_map[num] = index

        for index, num in enumerate(nums):
            if target - num in nums_map and index != nums_map[target-num]:
                return [index,nums_map[target-num]]
"""