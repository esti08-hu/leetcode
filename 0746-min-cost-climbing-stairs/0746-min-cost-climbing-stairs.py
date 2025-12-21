class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        [1,100,1,1,1,100,1,1,100,1]
        [1,100,2,3,3,103,4,5,104,6]
        dp = [2, 100]
        '''

        dp = [cost[0],cost[1]]
        
        for i in range(2, len(cost)):
            tmp = dp[1]
            dp[1] = min(dp) + cost[i]
            dp[0] = tmp
        return min(dp)
