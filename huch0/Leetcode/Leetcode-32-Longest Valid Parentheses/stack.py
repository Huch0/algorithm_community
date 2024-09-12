class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s == '':
            return 0
        stack = [-1]
        max_len = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()  # Pop for matching ')'
                if not stack:
                    stack.append(i)  # If stack is empty, push current index as the base
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len
