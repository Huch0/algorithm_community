class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(subset: List[int], index: int):
            # Prevent subset.append(nums[-1]) in first function call
            if index >= 0:
                subset.append(nums[index])
            subsets.append(subset[:])
            
            # base case : all traversal ends in last element
            if (index == len(nums) - 1):
                return
            
            for i in range(index + 1, len(nums)):
                dfs(subset[:], i)
        
        subsets = []
        nums.sort()
        dfs([], -1)

        return subsets
