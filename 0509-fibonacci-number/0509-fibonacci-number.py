class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n 
            
        dp = [0,1]

        i = 2

        while i <= n:
            tmp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = tmp

            i+=1
        
        return dp[1]
