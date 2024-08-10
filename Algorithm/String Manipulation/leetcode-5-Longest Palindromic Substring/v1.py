class Solution:
    def longestPalindrome(self, s: str) -> str:
        def seek_longest(j):
            longest_substring = s[0]
            for i in range(len(s) - j):
                start, end = i, i+j
                while start > -1 and end < len(s):
                    substring = s[start:end+1]
                    if substring != substring[::-1]:
                        break
                    longest_substring = max(longest_substring, substring, key = len)
                    start, end = start - 1, end + 1
            return longest_substring
        return max(seek_longest(1), seek_longest(2), key = len)
