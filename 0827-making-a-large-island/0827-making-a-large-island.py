class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        '''
        
        '''
        rows, cols = len(grid), len(grid[0])
        def bfs(r, c, isl_num):
            q = deque()
            q.append((r, c))
            self.main_visited.add((r, c))
            grid[r][c] = isl_num
            curr_area = 1

            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    directions = [[1,0],[-1,0],[0,1],[0,-1]]
                    for dr, dc in directions:
                        nr, nc = row+dr, col+dc
                        if (nr in range(rows) and 
                            nc in range(cols) and 
                            (nr, nc) not in self.main_visited and 
                            grid[nr][nc]):

                            q.append((nr, nc))
                            self.main_visited.add((nr, nc))
                            grid[nr][nc] = isl_num
                            curr_area += 1

            return curr_area
            
        isl_num = 1
        island_dict = {}
        self.main_visited = set()
        flag = False
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and (r, c) not in self.main_visited:
                    area = bfs(r, c, isl_num)
                    island_dict[isl_num] = area
                    isl_num+=1
                if not flag and not grid[r][c]:
                    flag = True
        if not flag:
            return rows*cols
            
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if not grid[r][c]:
                    directions = [[1,0],[-1,0],[0,1],[0,-1]]
                    curr_area = 0
                    added = set()
                    
                    for dr, dc in directions:
                        nr, nc = r+dr, c+dc
                        if nr in range(rows) and nc in range(cols) and grid[nr][nc] in island_dict and grid[nr][nc] not in added:
                                curr_area += island_dict[grid[nr][nc]]
                                added.add(grid[nr][nc])
                    max_area = max(max_area, curr_area)
        
        return max_area + 1



