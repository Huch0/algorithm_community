# reference: https://leetcode.com/problems/longest-palindromic-substring/solutions/4212564/beats-96-49-5-different-approaches-brute-force-eac-dp-ma-recursion/?envType=study-plan-v2&envId=top-100-liked
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        max_len = 1
        max_str = s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = True  # Every single character is palindrome
            for j in range(i):
                if s[j] == s[i] and (i - j <= 2 or dp[j + 1][i - 1]):
                    # s[j:i + 1] is palindrome if
                    # 1. s[j] == s[i] and
                    # 2. s[j + 1:i] is palindrome or len(substr) <= 3, in which case the substr is palindrome if s[j] == s[i]
                    dp[j][i] = True
                    if i - j + 1 > max_len:
                        max_len = i - j + 1
                        max_str = s[j:i + 1]

        return max_str
