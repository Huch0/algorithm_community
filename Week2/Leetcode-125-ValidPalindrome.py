# rewritten Faster code
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_case = []  
        
        for i in s.lower():
            if i.isalnum() :
                lower_case.append(i)

        print(lower_case)
        print(list(reversed(lower_case)))
        if lower_case == list(reversed(lower_case)) : return True
        else : False


""" 
# first summit

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_case = []  
        
        for i in s.lower():
            if i.isalnum() :
                lower_case.append(i)


        left = 0
        right = len(lower_case)-1
        print(lower_case)

        while True:
            if len(lower_case) == 0 : return True
            if right <= left : break

            if lower_case[left] != lower_case[right] : return False
            print(lower_case[left])
            
            left += 1
            right -= 1

        return True
"""