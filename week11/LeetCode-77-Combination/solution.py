class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def dfs(combinations: List[int], src: int, k: int, result: List[List[int]]) -> None:
            if len(combinations) == k:
                result.append(combinations[:])
                return

            for i in range(src, n+1):
                combinations.append(i)
                dfs(combinations, i+1, k, result)
                combinations.pop()

        dfs([], 1, k, result)
        return result
