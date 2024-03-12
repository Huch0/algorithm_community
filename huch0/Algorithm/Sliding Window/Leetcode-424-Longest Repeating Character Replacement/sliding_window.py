class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counter = Counter()
        longest = 0  # The length of longest substring
        max_freq = 0  # The counter of most frequent character
        l, r = 0, 0
        while r < len(s):
            char_counter[s[r]] += 1
            max_freq = max(max_freq, char_counter[s[r]])
            if max_freq + k >= r - l + 1:
                longest = r - l + 1
            else:
                # Move the left pointer to the right
                char_counter[s[l]] -= 1
                l += 1
            r += 1

        return longest
