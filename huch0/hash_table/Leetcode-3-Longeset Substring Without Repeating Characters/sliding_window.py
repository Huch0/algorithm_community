class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_length = 0
        char_index = {}

        left = 0  # Left boundary of the sliding window

        for right in range(n):
            # If the current character is in the char_index dictionary
            # and its index is greater than or equal to the left boundary,
            # update the left boundary to the next index of the character.
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1

            # Update the index of the current character in the char_index dictionary
            char_index[s[right]] = right

            # Calculate the current substring length
            current_length = right - left + 1

            # Update the maximum length if needed
            max_length = max(max_length, current_length)

        return max_length
