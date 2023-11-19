from itertools import combinations

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        for i in range(len(nums)+1):
            print(list(combinations(nums, i)))
            result += list(combinations(nums, i))
        return result