class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        cache = {}
        def dfs(i, j):
            if i < 0 or j < 0 or j > i:
                return 0.0
            if i == 0 and j == 0:
                return poured
            if (i, j) in cache:
                return cache[(i, j)]
            
            left = max(0, (dfs(i-1, j-1)-1)/2.0)
            right = max(0, (dfs(i-1, j)-1)/2.0)

            cache[(i, j)] = left+right
            return cache[(i, j)]
        
        return min(1, dfs(query_row, query_glass))

