class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hd = 0
        diff = x ^ y
        while diff > 0:
            if diff & 1 == 1:
                hd += 1
            diff >>= 1

        return hd
