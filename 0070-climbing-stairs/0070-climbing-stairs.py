class Solution:
    def climbStairs(self, n: int) -> int:
        @cache

        def dp(i):
            if i < 0:
                return 0
            if i == 0:
                return 1
            
            s1 = dp(i-1)
            s2 = dp(i-2)
            return s1+s2
        
        return dp(n)
