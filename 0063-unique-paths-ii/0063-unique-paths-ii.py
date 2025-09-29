class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        cache = {}

        def dfs(i, j):
            if i<0 or j <0 or i>=row or j >= col or obstacleGrid[i][j] == 1:
                return 0
            
            if i==row-1 and j ==col-1:
                return 1
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            right = dfs(i, j+1)
            down = dfs(i+1, j)

            cache[i, j] = right + down

            return cache[(i, j)]
        
        ans =  dfs(0,0)

        return ans