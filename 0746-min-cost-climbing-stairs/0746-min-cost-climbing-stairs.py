class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dp(i):
            if i >=len(cost):
                return 0

            step1 = cost[i]+dp(i+1)
            step2 = cost[i]+dp(i+2)

            return min(step1, step2)
        
        s0 = dp(0)
        s1 = dp(1)
        return min(s0, s1)