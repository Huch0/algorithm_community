from collections import defaultdict

class Solution:
    def fib(self, n: int) -> int:
        # Tablulation
        dp = [0, 1]

        if n < 2:
            return dp[n]
        
        for i in range(2, n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]
    
        # Memoization
    
        #dp = defaultdict(int)

        if n < 2:
            return n

        if dp[n]:
            return dp[n]
        
        dp[n] = self.fib(n-1) + self.fib(n-2)

        return dp[n]