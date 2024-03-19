class Solution(object):
    def lengthOfLongestSubstring(self, s):
        word = {}
        result = 0
        start = 0

        for idx, char in enumerate(s):
            #start <= word[char] : char that appeared but not in this sliding window
            if char in word and start <= word[char]:
                start = word [char] +1
            else:
                result = max(result, idx - start + 1)

            word[char] = idx
            
        return result