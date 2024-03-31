class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        # if a number XOR twice, it will be 0
        # so the result will be the single number
        for num in nums:
            result ^= num
        return result
