class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        grid_len = len(grid)
        row = [" "] * (grid_len * 3)
        new_grid = [row[:] for i in range(grid_len * 3)]

        rows, cols = grid_len, grid_len
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "\\":
                    nr, nc = r*3, c*3
                    new_grid[nr+0][nc+0] = "x"
                    new_grid[nr+1][nc+1] = "x"
                    new_grid[nr+2][nc+2] = "x"
                elif grid[r][c] == "/":
                    nr, nc = r*3, c*3
                    new_grid[nr+0][nc+2] = "x"
                    new_grid[nr+1][nc+1] = "x"
                    new_grid[nr+2][nc+0] = "x"
                    
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        n = grid_len * 3
        def dfs(r, c):
            if r < 0 or r == n or c < 0 or c == n or new_grid[r][c] == "x":
                return 
            
            new_grid[r][c] = "x"

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                dfs(nr, nc)
            
        count = 0
        for i in range(n):
            for j in range(n):
                if new_grid[i][j] == " ":
                    dfs(i, j)
                    count += 1
        
        return count
        
