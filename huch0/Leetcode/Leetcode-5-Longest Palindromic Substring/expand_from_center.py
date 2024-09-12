# reference: https://leetcode.com/problems/longest-palindromic-substring/solutions/4212564/beats-96-49-5-different-approaches-brute-force-eac-dp-ma-recursion/?envType=study-plan-v2&envId=top-100-liked
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand_from_center(left, right):
            while 0 <= left and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  # since while loop breaks when s[left:right + 1]

        max_str = s[0]

        for i in range(len(s) - 1):
            # Consider only the ith character as a center
            odd = expand_from_center(i, i)
            # Consider ith and i + 1th character as a center
            even = expand_from_center(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str
