class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        binary = x^y
        result = bin(binary)
        return result.count("1")