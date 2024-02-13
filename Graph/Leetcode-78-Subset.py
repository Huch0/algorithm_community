class Solution(object):
    def subsets(self, nums):
        results = []
        def dfs(idx, path):
            results.append(path)
            for i in range(idx, len(nums)):
                dfs(i+1, path+[nums[i]])
        dfs(0,[])
        return results