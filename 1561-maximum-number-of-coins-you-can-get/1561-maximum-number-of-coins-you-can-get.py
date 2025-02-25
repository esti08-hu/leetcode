class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)

        coins = 0
        for i in range(len(piles) // 3):
            coins += piles[2 * i + 1]
        return coins