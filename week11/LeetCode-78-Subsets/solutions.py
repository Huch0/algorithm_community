class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index_of_list, path):
            result.append(path[:])
            for i in range(index_of_list, length):
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()

        result = []
        path = []
        index_of_list = 0
        length = len(nums)

        dfs(index_of_list, path)

        return result