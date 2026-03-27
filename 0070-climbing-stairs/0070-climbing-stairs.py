class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dfs(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            
            return dfs(n-1) + dfs(n-2)
        
        return dfs(n)