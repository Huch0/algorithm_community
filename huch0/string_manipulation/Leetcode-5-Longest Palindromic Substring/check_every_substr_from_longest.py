class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        for i in range(n):
            for j in range(i + 1):
                # take substr from longest
                substr = s[j : n - (i - j)]

                #print(i, j, substr)
                
                # Check substr is palindrome
                k = 0
                while(k < len(substr)//2 ):
                    #print(substr, k, substr[k], substr[-(k + 1)])
                    if substr[k] != substr[-(k + 1)]:
                        break
                    k += 1
                if k == len(substr) // 2:
                    return substr

        
        return ""