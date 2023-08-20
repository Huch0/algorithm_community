class Solution(object):
    def longestPalindrome(self, s):
        for i in range(len(s)):
            for j in range(i + 1):
                temp = s[j : len(s) - i + j]
                if temp[:] == temp[::-1]:
                    return temp

        return ""

# def Solution(object):
#     def longestPalindrome(self, s):
#         def expand(left: int, right: int) -> str:
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#             return s[left + 1:right]

#         if  lens(s) < 2 or s == s[::-1]:
#             return s
        
#         result = ''

#         for i in range(len(s) - 1):
#             result = max(result,
#                             expand(i, i + 1),
#                             expand(i, i + 2),
#                             key=len)
#         return result