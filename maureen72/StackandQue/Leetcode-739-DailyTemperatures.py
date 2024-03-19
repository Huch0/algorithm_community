class Solution(object):
    def dailyTemperatures(self, temperatures):
        T = temperatures
        n = len(T)
        result = [0] * n
        stack = []

        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                tmp = stack.pop()
                result[tmp] = i - tmp
            stack.append(i)
        return result