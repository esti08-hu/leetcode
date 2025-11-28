class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or r == rows or c == cols or 
                not grid2[r][c]):
                return 
            if grid2[r][c] and not grid1[r][c]:
                self.flag = False
            grid2[r][c] = 0
            
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                dfs(r+dr, c+dc)
        
        sub_island = 0
        for r in range(rows):
            for c in range(cols):
                if grid1[r][c] and grid2[r][c]:
                    self.flag = True
                    dfs(r, c)
                    print(self.flag, (r, c))
                    if self.flag:
                        sub_island+=1
        
        return sub_island

