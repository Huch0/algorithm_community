class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        max_palindrome = ""
        
        for i in range(len(s)):
            odd_palindrome = expand_around_center(i, i)
            even_palindrome = expand_around_center(i, i+1)
            
            if len(odd_palindrome) > len(even_palindrome):
                current_longest = odd_palindrome
            else:
                current_longest = even_palindrome
            
            if len(current_longest) > len(max_palindrome):
                max_palindrome = current_longest
        
        return max_palindrome
