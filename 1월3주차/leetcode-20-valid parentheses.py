class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mydict = {
            '(':')',
            '[':']',
            '{':'}'
        }
        for c in s:
            if c in mydict:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if c != mydict.get(stack.pop()):
                    return False
                    
        if len(stack) == 0:
            return True
        else:
            return False