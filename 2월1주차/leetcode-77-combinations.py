class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        myset = []
        answer = []
        def dfs(i):
            if len(myset) == k:
                answer.append(myset[:])
                return
            for cur in range(i, n+1):
                myset.append(cur)
                dfs(cur+1)
                myset.pop()

        dfs(1)
        return answer