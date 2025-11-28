class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        '''
        island never in border
        if grid val == 0 and on border 
            valid = False
        '''
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if (grid[r][c] or (r, c) in visited):
                return 
            visited.add((r, c))

            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if nr < 0 or nc < 0 or nr == rows or nc == cols:
                    continue
                if not grid[nr][nc] and self.valid and (nr == 0 or nr == rows-1 or nc == 0 or nc == cols-1):
                    self.valid = False
                    
                dfs(nr, nc)

        closed_island = 0
        for r in range(1, rows-1):
            for c in range(1, cols-1):
                if not grid[r][c] and (r, c) not in visited:
                    self.valid = True
                    dfs(r, c)
                    if self.valid:
                        closed_island += 1
        
        return closed_island

