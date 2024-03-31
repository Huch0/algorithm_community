class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(path):
            # base case
            if len(path) == len(nums):
                # Copy path not to share same reference in permutations
                permutations.append(path[:])
                return
            
            # Add possible cases
            for num in nums:
                if num not in path:
                    path.append(num)
                    dfs(path)
                    path.pop()
            
        permutations = []
        dfs([])

        return permutations
        