class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        c = [float("inf")]*(amount+1)
        c[0] = 0
        for a in range(1, amount+1):
            for coin in coins:
                if a - coin >= 0:
                    c[a] = min(1+c[a-coin], c[a])
        print(c)
        return -1 if c[amount] == float("inf") else c[amount]