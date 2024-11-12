def solution(s):
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
            
    if len(stack) == 0:
        return True
    else:
        return False