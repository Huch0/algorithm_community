def is_palindrome(s: str) -> bool:
    return s == s[::-1]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        result = []

        for start in range(length):
            for end in range(length - 1, start, -1):
                if(start == end):
                    break
                if(s[start] == s[end]):
                    if(is_palindrome(s[start : end+1])):
                        result.append(s[start : end+1])
                else:
                    pass
        
        if (result == []):
            return(s[0])
        
        else:
            return max(result, key=len)