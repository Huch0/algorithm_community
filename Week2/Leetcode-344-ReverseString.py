class Solution:
    def reverseString(self, s: List[str]) -> None:

        left = 0
        right = len(s)-1

        while True :
            if right <= left : break
            s[left], s[right] = s[right], s[left]
            
            left += 1
            right -= 1

"""
#Pythonic code

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
"""