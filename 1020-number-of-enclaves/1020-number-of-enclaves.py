class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        rows, cols = len(grid), len(grid[0])
        def borderDfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0:
                return 
            
            grid[r][c] = 0

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                borderDfs(nr, nc)
        
        for i in range(rows):
            if grid[i][0]:
                borderDfs(i, 0)
            if grid[i][cols-1]:
                borderDfs(i, cols-1)

        for j in range(cols):
            if grid[0][j]:
                borderDfs(0, j)
            if grid[rows-1][j]:
                borderDfs(rows-1, j)

        self.count = 0
        def dfs(r, c, cnt):
            if r < 1 or r == rows - 1 or c < 1 or c == cols - 1 or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            self.count += 1


            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                dfs(nr, nc, cnt)
            
            return cnt 
                
        for i in range(1, rows-1):
            for j in range(1, cols - 1):
                if grid[i][j]:
                    dfs(i, j, 0)

        return self.count
            