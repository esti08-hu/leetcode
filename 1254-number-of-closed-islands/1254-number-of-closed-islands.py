class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = 1

            while q:
                for i in range(len(q)):
                    row, col = q.popleft()

                    directions = [[1,0], [-1,0], [0,1], [0,-1]]
                    for dr, dc in directions:
                        nr, nc = row+dr, col+dc
                        if (nr in range(rows) and 
                            nc in range(cols) and 
                            not grid[nr][nc]):
                            q.append((nr, nc))
                            grid[nr][nc] = 1

        for r in range(rows):
            if not grid[r][0]:
                bfs(r, 0)

        for r in range(rows):
            if not grid[r][cols-1]:
                bfs(r, cols-1)

        for c in range(cols):
            if not grid[0][c]:
                bfs(0, c)

        for c in range(cols):
            if not grid[rows-1][c]:
                bfs(rows-1, c)
        
        closed_island = 0

        for r in range(1, rows-1):
            for c in range(1, cols-1):
                if not grid[r][c]:
                    bfs(r, c)
                    closed_island += 1
        
        return closed_island
