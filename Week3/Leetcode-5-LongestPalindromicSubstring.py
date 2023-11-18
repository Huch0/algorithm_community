# rewritten Faster code
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while True :
                if left < 0 or right >= len(s) or s[left] != s[right] : break
                left -= 1
                right += 1
            return s[left+1:right]
        
        if len(s) < 2 : return s 

        result = ""
        for i in range(len(s)-1) :
            result = max(result, expand(i,i+1),expand(i,i+2), key = len)
        
        return result


""" 
# first summit

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def odd_palindrome (s: str) -> list :
            odd_palindrome_list = []     
            for i in range(len(s)):
                for j in range(1000):
                    if i-j < 0 or i+j >= len(s) : break
                    if s[i-j] != s[i+j] : break
                odd_palindrome_list.append([2*j-1,i])

            print(odd_palindrome_list)
            
            return max(odd_palindrome_list)
                
        
        def even_palindrome(s: str) -> list:
            even_palindrome_list = []
            for i in range(len(s)):
                for j in range(1000):
                    if i-j < 0 or i+j+1 >= len(s) : break
                    if s[i-j] != s[i+j+1] : break
                if j == 0 : even_palindrome_list.append([1,i])
                else : even_palindrome_list.append([2*j,i])
            return max(even_palindrome_list)
        
        longest_palindrome = max(odd_palindrome(s),even_palindrome(s))
        print(longest_palindrome)
        if len(s) == 1 : return s
        else:
            if longest_palindrome[0]%2 == 0 : return s[longest_palindrome[1]-longest_palindrome[0]//2+1:longest_palindrome[1]-longest_palindrome[0]//2+1 + longest_palindrome[0]]
            else : 
                print((longest_palindrome[0]+1)//2)
                return s[longest_palindrome[1]-((longest_palindrome[0]-1)//2) : longest_palindrome[1]+((longest_palindrome[0]-1)//2)+1]
"""