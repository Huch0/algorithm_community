class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        # base case
        dp[0][0] = grid[0][0]
        s = grid[0][0]
        for j in range(1, n):
            s += grid[0][j]
            dp[0][j] = s
        s = grid[0][0]
        for i in range(1, m):
            s += grid[i][0]
            dp[i][0] = s

        # dp iteration
        for i in range(1, m):
            for j in range(1, n):
                up = dp[i - 1][j]
                left = dp[i][j - 1]
                dp[i][j] = min(up, left) + grid[i][j]

        return dp[m - 1][n - 1]
