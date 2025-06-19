from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        directions = {
            1: [(0, -1), (0, 1)],  
            2: [(-1, 0), (1, 0)],  
            3: [(0, -1), (1, 0)],  
            4: [(0, 1), (1, 0)],   
            5: [(0, -1), (-1, 0)], 
            6: [(0, 1), (-1, 0)]   
        }
        
        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n
        
        def can_connect(from_dir, to_dir, dx, dy):
            return (-dx, -dy) in directions[to_dir]
        
        visited = set()
        
        def dfs(x, y):
            if (x, y) in visited:
                return False
            visited.add((x, y))
            
            if x == m - 1 and y == n - 1:
                return True
            
            for dx, dy in directions[grid[x][y]]:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny) and can_connect(grid[x][y], grid[nx][ny], dx, dy):
                    if dfs(nx, ny):
                        return True
            
            return False
        
        return dfs(0, 0)