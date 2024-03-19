class Solution(object):
    def maxProfit(self, prices):

        profit = 0
        minPrice = float('inf')
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > profit:
                profit = prices[i] - minPrice
                
        return profit