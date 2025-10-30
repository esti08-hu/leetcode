class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0.0] * (i + 1) for i in range(query_row + 1)]
        dp[0][0] = poured

        for i in range(query_row):
            for j in range(i+1):
                if dp[i][j] > 1:
                    extra = (dp[i][j]-1)/2.0
                    dp[i+1][j] += extra
                    dp[i+1][j+1] += extra
                
        return min(1, dp[query_row][query_glass])