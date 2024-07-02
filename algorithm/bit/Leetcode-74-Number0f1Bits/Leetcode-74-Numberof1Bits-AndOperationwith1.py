class Solution:
    def hammingWeight(self, n: int) -> int:
        check = 0
        result = 0

        while n != 0 :
            check = (n&1)
            result += check
            n = (n >> 1)
        
        return result