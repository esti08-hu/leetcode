class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = "0"

            while q:
                for i in range(len(q)):
                    row, col = q.popleft()

                    directions = [(0,1), (0,-1), (1,0), (-1,0)]
                    for dr,dc in directions:
                        nr, nc = row + dr, col + dc

                        if nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1":
                            grid[nr][nc] = "0"
                            q.append((nr, nc))
        
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands+=1
        
        return islands
