class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hd = x ^ y
        result = 0
        while hd > 0:
            if (hd & 0b1 == 0b1):
                result += 1
            hd = hd >> 1

        return result