class Solution:
    def isPalindrome(self, s: str) -> bool:
        preprocessed = []

        for c in s:
            if c.isalnum():
                preprocessed.append(c.lower())

        #print(preprocessed)
        for i in range(len(preprocessed) // 2):
            if preprocessed[i] != preprocessed[len(preprocessed) - 1 - i]:
                return 0

        return 1