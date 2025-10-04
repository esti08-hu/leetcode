class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        memo = [[-1]*n for i in range(n)]

        def dfs(i, j):
            if i==j:
                return piles[i]
            
            if memo[i][j] != -1:
                return memo[i][j]

            diff1 = piles[i]-dfs(i+1, j)
            diff2 = piles[j]-dfs(i, j-1)

            res = max(diff1, diff2)
            memo[i][j] = res

            return memo[i][j]
            
        return dfs(0, n-1)>=0
