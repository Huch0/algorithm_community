class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(n + 1)]

        dp[0] = True

        for i in range(1, n + 1):
            for w in wordDict:
                if i - len(w) >= 0 and dp[i - len(w)] and w == s[i - len(w):i]:
                    dp[i] = True

        return dp[n]
