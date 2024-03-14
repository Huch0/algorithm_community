class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # solution 1
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
    
        # solution 2
        