class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows, cols = len(word1), len(word2)
        if not word1 or not word2:
            return max(rows, cols)
            
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(rows+1):
            dp[i][0] = i
        for j in range(cols+1):
            dp[0][j] = j

        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    insert = dp[i][j-1]
                    delete = dp[i-1][j]
                    replace = dp[i-1][j-1]

                    dp[i][j] = 1 + min(insert, delete, replace)
        print(dp)
        return dp[rows][cols]
