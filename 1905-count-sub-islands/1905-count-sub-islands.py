class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])

        visited = set()
        def bfs(r, c):

            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    directions = [[1,0],[-1,0],[0,1],[0,-1]]
                    for dr, dc in directions:
                        nr, nc = row+dr, col+dc
                        if (nr in range(rows) and 
                            nc in range(cols)):

                            if ((nr, nc) not in visited and 
                                grid1[nr][nc] and grid2[nr][nc]):
                                q.append((nr, nc))
                                visited.add((nr, nc))
                            
                            if self.flag and grid2[nr][nc] and not grid1[nr][nc]:
                                self.flag = False

        self.sub_islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid1[i][j] and grid2[i][j] and (i, j) not in visited:
                    self.flag = True
                    bfs(i, j)

                    if self.flag:
                        self.sub_islands += 1
                    
        return self.sub_islands
