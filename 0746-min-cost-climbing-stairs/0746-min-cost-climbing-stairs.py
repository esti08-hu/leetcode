class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [cost[-1], 0]

        for i in range(len(cost)-2, -1, -1):
            tmp = dp[0]
            dp[0] = cost[i]+min(dp)
            dp[1]=tmp

        return min(dp)

            
