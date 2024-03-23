class Solution:
    def fib(self, n: int) -> int:
        tmp1, tmp2 = 0, 1
        if n <= 1:
            return n

        for i in range(2, n + 1):
            tmp1, tmp2 = tmp2, tmp1 + tmp2

        return tmp2
