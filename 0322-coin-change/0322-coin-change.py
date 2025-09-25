class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]+[float("inf")] * (amount)

        for a in range(1, amount+1):
            for c in coins:
                if a >= c:
                    dp[a] = min(dp[a], dp[a-c]+1)
        return -1 if dp[-1]==float("inf") else dp[-1]