class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols:
                return False
            
            if grid[r][c] != 0:
                return True
            
            grid[r][c] = 1
            
            down = dfs(r+1, c) 
            up = dfs(r-1, c) 
            right = dfs(r, c+1) 
            left = dfs(r, c-1)
            
            return right and left and up and down
        
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    if dfs(r, c):
                        count += 1
        
        return count