class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b & 0xFFFFFFFF:
            c = a ^ b
            b = (a & b) << 1
            a = c

        a = a & 0xFFFFFFFF
        if a >= 0x80000000:
            return ~(a ^ 0xFFFFFFFF)
        return a