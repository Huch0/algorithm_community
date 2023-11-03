class Solution(object):
    def reverseString(self, s):
        left_idx = 0
        right_idx = len(s)-1

        while left_idx < right_idx:
            tmp = s[left_idx]
            s[left_idx] = s[right_idx]
            s[right_idx] = tmp
            left_idx += 1
            right_idx -= 1
        