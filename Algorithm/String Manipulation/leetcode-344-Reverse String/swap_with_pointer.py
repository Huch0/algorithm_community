class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < len(s) // 2 : #left < right !!
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
