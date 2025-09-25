class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]+[float("inf")] * (amount)

        print(dp)
        for c in coins:
            for i in range(1, amount+1):
                if i >= c:
                    dp[i] = min(dp[i], dp[i-c]+1)
        return -1 if dp[-1]==float("inf") else dp[-1]