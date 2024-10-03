class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # if word1[i - 1] == word2[j - 1]: no need to change
        # distance = min(up, left, up_left) + 1
        # dp[i - 1][j] + 1: delete ith character from word1
        # dp[i][j - 1] + 1: insert jth character of word2 to word1
        # dp[i - 1][j - 1] + 1: replace ith character of word1 with jth character of word2

        # ex1:
        #     -   r   o   s
        # -   0   1   2   3
        # h   1   1   2   3
        # o   2   2   1   2
        # r   3   2   2   2
        # s   4   3   3   2
        # e   5   4   4   3

        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # base case
        for i in range(1, m + 1):
            dp[i][0] = i  # deleting characters from word1
        for j in range(1, n + 1):
            dp[0][j] = j  # inserting characters into word1

        # dp iteration
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # no change needed if the characters are the same
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,  # deletion
                        dp[i][j - 1] + 1,  # insertion
                        dp[i - 1][j - 1] + 1  # replacement
                    )

        return dp[m][n]
