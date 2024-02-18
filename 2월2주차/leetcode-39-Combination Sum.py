class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        mylist = []
        def dfs(startIndex):
            if sum(mylist) == target:
                answer.append(mylist[:])
                return
            elif sum(mylist) > target:
                return

            for i in range(startIndex, len(candidates)):
                mylist.append(candidates[i])
                dfs(i)
                mylist.pop()

        dfs(0)
        return answer