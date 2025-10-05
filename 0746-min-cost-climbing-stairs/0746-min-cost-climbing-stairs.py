class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def dp(i):
            if i >=len(cost):
                return 0
            if i in cache:
                return cache[i]

            step1 = cost[i]+dp(i+1)
            step2 = cost[i]+dp(i+2)

            step = min(step1, step2)
            cache[i] = step
            return step
        
        s0 = dp(0)
        s1 = dp(1)
        return min(s0, s1)