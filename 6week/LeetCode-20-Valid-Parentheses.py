class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for char in s:
            #여는 괄호인 경우
            if char not in table:
                stack.append(char)
            #닫는 괄호인 경우
            elif len(stack) == 0 or table[char] != stack.pop():
                return False
            
        if len(stack) == 0:
            return True
        else:
            return False
