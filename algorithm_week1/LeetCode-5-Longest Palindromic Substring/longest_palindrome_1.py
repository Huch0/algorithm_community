class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def is_palindrome(check_str: str) -> bool:
            return check_str == check_str[::-1]
        
        longest_palindrome = ""
        
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
            
                substring = s[i:j]
                if is_palindrome(substring) and len(substring) > len(longest_palindrome):
                    longest_palindrome = substring
        
        return longest_palindrome
