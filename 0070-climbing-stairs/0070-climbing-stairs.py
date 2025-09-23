class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = {1:1, 2:2}
        
        def dfs(n):
            if n in self.memo:
                return self.memo[n]

            left = dfs(n-1)
            right = dfs(n-2)
            self.memo[n] = left + right
            return self.memo[n]
            
        return dfs(n)