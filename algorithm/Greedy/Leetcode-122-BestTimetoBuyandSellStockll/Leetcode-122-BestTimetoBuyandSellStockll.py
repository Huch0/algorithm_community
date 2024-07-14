class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        for i in range(len(prices)-1) :
            benefit = prices[i+1] - prices[i]
            if benefit > 0 : result += benefit

        return result