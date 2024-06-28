class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0XFFFFFFFF
        INT_MAX = 0X7FFFFFFF

        a_bin = bin(a & MASK)[2:].zfill(32)
        b_bin = bin(b & MASK)[2:].zfill(32)

        carry = 0
        Sum = 0

        result = []

        for i in range(32) :
            a_bit = int(a_bin[31-i])
            b_bit = int(b_bin[31-i])

            Q1 = a_bit & b_bit
            Q2 = a_bit ^ b_bit
            Q3 = Q2 & carry
            Sum = Q2 ^ carry
            carry = Q1 | Q3

            result.append(str(Sum))
        
        num = int(''.join(result[::-1]),2) & MASK
    
        if num > INT_MAX :
            num = -((num ^ MASK) + 1)
        
        return num 