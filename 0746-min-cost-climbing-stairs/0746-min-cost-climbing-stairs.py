class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache

        def dfs(idx):
            if idx >= len(cost):
                return 0
            
            return cost[idx] + min(dfs(idx + 1), dfs(idx+2))
        
        return min(dfs(0), dfs(1))
        
