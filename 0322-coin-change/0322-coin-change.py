class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(amt):
            if amt == 0:
                return 0
            if amt < 0:
                return float("inf")
            if amt in cache:
                return cache[amt]

            min_coins = float("inf")
            for c in coins:
                res = dfs(amt - c)
                if res != float("inf"):
                    min_coins = min(min_coins, res + 1)

            cache[amt] = min_coins
            return min_coins

        ans = dfs(amount)
        return -1 if ans == float("inf") else ans
