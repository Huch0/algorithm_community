# faster code 

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = { '(' : ')', '{' : '}', '[' : ']' }

        for char in s :
            if char in dic.keys() : stack.append(char)
            else : 
                if len(stack) == 0 or dic[stack.pop()] != char: return False

        return len(stack) == 0

"""
first commit 

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = { '(' : ')', '{' : '}', '[' : ']' }

        for char in s :
            if char in dic.keys() : stack.append(char)
            else : 
                if len(stack) == 0 or dic[stack.pop()] != char: return False

        if len(stack) == 0 : return True
        else : return False
"""