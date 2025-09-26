class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float('inf')
        cache = {}
        
        def dp(a):
            if a == 0:
                return 0
            if a < 0:
                return INF
            if a in cache:
                return cache[a]
            
            min_coins = INF
            for c in coins:
                res = dp(a - c)
                if res != INF:
                    min_coins = min(min_coins, res + 1)
            cache[a] = min_coins
            return min_coins

        ans = dp(amount)
        return -1 if ans == INF else ans