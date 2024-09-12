class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]

        # base case
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    continue
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[m - 1][n - 1]
