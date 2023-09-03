class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = ""
        if len(s) == 1:
            return s
        else:
            for i in range(0, len(s)):
                check_odd = 0
                while (i - check_odd >= 0) and (i + check_odd < len(s)) and (s[i - check_odd] == s[i + check_odd]):
                    check_odd += 1

                check_odd -= 1
                if check_odd * 2 + 1 > len(max_palindrome):
                    max_palindrome =  s[i - check_odd : i + check_odd + 1]

                check_even = 0
                while (i - check_even >= 0) and (i + 1 + check_even < len(s)) and (s[i - check_even] == s[i + 1 + check_even]):
                    check_even += 1

                if check_even * 2 > len(max_palindrome):
                    check_even -= 1
                    max_palindrome =  s[i - check_even : i + check_even + 2]

            return max_palindrome