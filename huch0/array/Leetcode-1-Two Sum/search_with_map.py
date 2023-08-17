class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. Convert nums list to hash table.
        nums_map = {}
        for i, n in enumerate(nums):
            nums_map[n] = i
        
        # 2. Find (target - num) for each numbers in nums
        for i, num in enumerate(nums):
            if (target - num) in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]

        return []