class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                skip_left = s[i+1:j+1] == s[i+1:j+1][::-1]
                skip_right = s[i:j] == s[i:j][::-1]
                
                return skip_left or skip_right
            
            i, j = i+1, j-1
        
        return True
