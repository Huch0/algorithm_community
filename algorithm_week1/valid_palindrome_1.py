class Solution:
    def parseString(self, s: str) -> str:
        s = s.lower()
        parsed = ""
        for char in s:
            if char.isalnum():
                parsed += char
        return parsed

    def reverseString(self, s: str) -> str:
        return s[::-1]

    def isPalindrome(self, s: str) -> bool:
        parsed = self.parseString(s)
        reversed_s = self.reverseString(parsed)
        return parsed == reversed_s
