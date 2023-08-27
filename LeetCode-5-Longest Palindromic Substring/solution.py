
def longestPalindrome(s: str) -> str:
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
                    print(max_palindrome + " odd")

                check_even = 0
                while (i - check_even >= 0) and (i + 1 + check_even < len(s)) and (s[i - check_even] == s[i + 1 + check_even]):
                    check_even += 1

                check_even -= 1
                if check_even * 2 > len(max_palindrome):
                    max_palindrome =  s[i - check_even : i + check_even + 2]
                    print(max_palindrome + " even")

            return max_palindrome


s = "cbbd"
print(longestPalindrome(s))
