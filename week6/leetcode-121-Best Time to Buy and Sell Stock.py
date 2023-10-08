import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = sys.maxsize
        answer = 0
        for price in prices:
            low = min(low, price)
            answer = max(answer, price - low)
        return answer
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        high, low = prices[0], prices[0]
        answer = high - low
        for price in prices[1:]:
            if price < low:
                low = price
                high = low + answer
            elif price > high:
                high = price
                answer = high - low
        return answer