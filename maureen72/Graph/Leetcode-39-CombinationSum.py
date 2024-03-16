class Solution(object):
    def combinationSum(self, candidates, target):
        results = []
        def dfs(index, path, csum):
            if csum > target:
                return
            if csum == target:
                results.append(path)
                return
            for i in range(index, len(candidates)):
                dfs(i, path + [candidates[i]], csum + candidates[i])
        dfs(0, [], 0)
        return results