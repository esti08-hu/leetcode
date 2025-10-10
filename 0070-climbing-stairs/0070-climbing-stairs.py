class Solution:
    def climbStairs(self, n: int) -> int:
        @cache

        def dp(i):
            if i > n:
                return 0
            if i == n:
                return 1
            
            s1 = dp(i+1)
            s2 = dp(i+2)
            return s1+s2
        
        return dp(0)
