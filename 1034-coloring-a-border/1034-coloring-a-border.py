class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def is_border(row, col):
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = row + dr, col + dc
                if not inbound(nr, nc) or grid[nr][nc] != originalColor:
                    return True
            return False
        
        visited = set()
        border_cells = set()
        originalColor = grid[row][col]
        
        def dfs(i, j):
            if not inbound(i, j) or (i, j) in visited or grid[i][j] != originalColor:
                return
            
            visited.add((i, j))
            
            if is_border(i, j):
                border_cells.add((i, j))
            
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                dfs(i + dr, j + dc)
        
        dfs(row, col)
        
        for i, j in border_cells:
            grid[i][j] = color
        
        return grid