class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0

        for i in range(len(prices) - 1):
            if prices[i] > prices[i + 1]:
                continue
            else:
                total_profit += prices[i + 1] - prices[i]

        return total_profit
