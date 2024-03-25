class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        profit = 0
        for i in range(1, days):
            cur_price = prices[i] - prices[i -1]
            if cur_price > 0:
                profit += cur_price
                
        return profit