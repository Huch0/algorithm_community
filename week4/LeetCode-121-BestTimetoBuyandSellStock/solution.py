class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, min_price = 0, float('inf')

        for price in prices:
            min_price, profit = min(price, min_price), max(profit, price - min_price)

        return profit