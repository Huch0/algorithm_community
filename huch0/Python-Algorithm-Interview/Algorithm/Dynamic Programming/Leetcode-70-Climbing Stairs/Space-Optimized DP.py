class Solution:
    def climbStairs(self, n: int) -> int:
        tmp1, tmp2 = 0, 1
        for i in range(1, n + 1):
            tmp1, tmp2 = tmp2, tmp1 + tmp2
        return tmp2
