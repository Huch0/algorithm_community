class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        length = len(candidates)
        result = []
        combinations = [] 
        sum_of_candidates = 0

        def dfs(sum_of_candidates: int, start: int) -> None:
            if sum_of_candidates == target:
                result.append(combinations[:])
                return
            elif sum_of_candidates > target:
                return

            for i in range(start, length):
                combinations.append(candidates[i])
                sum_of_candidates += candidates[i]
                dfs(sum_of_candidates, i)
                combinations.pop()
                sum_of_candidates -= candidates[i]

        dfs(sum_of_candidates, 0)
        return result