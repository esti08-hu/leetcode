class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(a):
            if a < 0:
                return float("inf")
            if a == 0:
                return 0
            
            curr_min = float("inf")
            for coin in coins:
                curr_min = min(curr_min, 1 + dfs(a - coin))
            
            return curr_min
        res = dfs(amount)
        return res if res != float("inf") else -1