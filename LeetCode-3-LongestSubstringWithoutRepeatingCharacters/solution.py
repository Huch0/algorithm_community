class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_length = 0
        char_index = {}

        for i in range(len(s)):
            char = s[i]
            if char in char_index and start <= char_index[char]:
                start = char_index[char] + 1
            else:
                max_length = max(max_length, i - start + 1)

            char_index[char] = i

        return max_length
