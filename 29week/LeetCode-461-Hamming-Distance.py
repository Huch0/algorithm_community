class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        #return bin(x^y).count('1')
        xor_result = x ^ y
        count = 0
        while xor_result:
            xor_result &= (xor_result - 1)  # 가장 오른쪽의 1 비트를 제거
            count += 1
        return count