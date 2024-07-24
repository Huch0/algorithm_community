class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = [x.lower() for x in s if x.isalnum()]
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True
