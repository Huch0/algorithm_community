class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        profit = 0

        for i in range(len(prices)-1):
            result = 0

            slice_prices = prices[i+1:]

            result = max(slice_prices) - prices[i]
            if profit < result:
                profit = result

        return profit