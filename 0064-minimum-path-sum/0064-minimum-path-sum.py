class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n,m=len(grid), len(grid[0])

        @cache
        def dp(i, j):
            if i==n or j==m:
                return float("inf")
            
            if i==n-1 and j==m-1:
                return grid[i][j]

            right = grid[i][j] + dp(i, j+1)
            down = grid[i][j] + dp(i+1, j)

            return min(down, right)
        
        return dp(0,0)
