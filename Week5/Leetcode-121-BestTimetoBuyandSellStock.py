# faster code 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        price_min = sys.maxsize

        for price in prices:
            if profit < price - price_min : profit = price - price_min
            if price_min > price : price_min = price
        
        return profit

"""
first commit 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price_min, price_max = prices[0], max(prices)
        max_profit = price_max - price_min

        for i in range(len(prices)) :
            if prices[i] < price_min : 
                price_min = prices[i]
                price_max = max(prices[i:])
                profit = price_max - price_min
                
                if max_profit < profit : max_profit = profit
            
        return max_profit

"""