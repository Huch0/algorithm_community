class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        profit = 0
        min_price = 10000

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit