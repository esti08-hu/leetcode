class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        cache = {}
        def dfs(d, state):
            if d == len(prices):
                return 0
            
            if (d, state) in cache:
                return cache[(d, state)]
            
            if state==0:
                buy = dfs(d+1, 1) - prices[d]
                skip = dfs(d+1, 0)
                cache[(d, state)] = max(buy, skip)
            elif state==1:
                buy = dfs(d+1, 2) + prices[d]
                skip = dfs(d+1, 1)
                cache[(d, state)] = max(buy, skip)
            elif state==2:
                cache[(d, state)] = dfs(d+1, 0)
            
            return cache[(d, state)]
        
        return dfs(0,0)
