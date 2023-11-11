class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(last_num: int, path: List):
            # Base case
            if len(path) == k:
                combinations.append(path[:])
                return

            # Do not need to iterate numbers less than or equal to last number of the path
            for num in range(last_num + 1, n + 1):
                path.append(num)
                dfs(num, path)
                path.pop()

        combinations = []

        dfs(0, [])

        return combinations
