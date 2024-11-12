class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buyPrice = prices[0]
        for i in range(len(prices)):
            if i == len(prices) - 1:
                if prices[i] > buyPrice:
                    profit += prices[i] - buyPrice
            elif prices[i + 1] < prices[i]:
                profit += prices[i] - buyPrice
                buyPrice = prices[i + 1]
        
        return profit