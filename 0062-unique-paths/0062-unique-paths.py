class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}

        def dfs(i, j):
            if i < 0 or j < 0 or i>=m or j>=n:
                return 0
            
            if i == m-1 and j == n-1:
                return 1
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            b = dfs(i+1, j) 
            r = dfs(i, j+1)
            cache[(i, j)] = b+r
            return cache[(i,j)]
        
        return dfs(0,0)

