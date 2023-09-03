class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, min_price = 0, min(prices)
        min_index = prices.index(min_price)
        for i in range(min_index, len(prices)):
            profit = max(profit, prices[i] - min_price)

        return profit