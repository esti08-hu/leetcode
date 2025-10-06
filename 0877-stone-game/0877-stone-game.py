class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        cache = {}

        def dp(i, j):
            if i == j:
                return piles[i]
            
            if (i, j) in cache:
                return cache[(i, j)]

            diff1 = piles[i] + dp(i+1, j)
            diff2 = piles[j] + dp(i, j-1)

            cache[(i, j)] = max(diff1, diff2)

            return cache[(i, j)]

        return dp(0, n-1) >= 0
