class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)

        stack = []
        for i in range(len(s)):
            if s[i] == ')':
                if len(stack) == 0:
                    stack = []
                    continue

                left = stack.pop()
                if s[left] != '(':
                    stack = []
                else:
                    dp[left], dp[i] = True, True
            else:
                stack.append(i)

            # print(i, stack)

        max_len = 0
        l, r = 0, 0
        while r < len(dp):
            if dp[r] == True:
                pass
            else:
                max_len = max(max_len, r - l)
                l = r + 1
            r += 1

        return max(max_len, r - l)
