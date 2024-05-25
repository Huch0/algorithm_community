def solution(s):
    stack = []

    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack or stack.pop() != '(':
                return False
    if len(stack) > 0:
        return False

    return True
