stack = [root]
while stack:
    if stack[-1].left:
        stack.append(stack[-1].left)
        stack[-1].left = None
        continue
    answer = min(answer, stack[-1].val - prev)
    prev = stack[-1].val
    if stack[-1].right:
        stack.append(stack[-1].right)
        stack.pop(-2)
    else:
        stack.pop(-1)
return answer