class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        unvisit = set()

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visit.add((r, c))

            time = -1
            while q:
                for i in range(len(q)):
                    row, col = q.popleft()

                    directions = [[1,0], [-1,0], [0,1], [0,-1]]
                    for dr, dc in directions:
                        r, c = row+dr, col+dc
                        if (r in range(ROWS) and
                            c in range(COLS) and
                            (r, c) not in visit and
                            grid[r][c] == 1):
                            q.append((r, c))
                            visit.add((r, c))
                            if (r, c) in unvisit:
                                unvisit.remove((r, c))

                time += 1
            return time

        total = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    total+=bfs(r, c)
                elif grid[r][c] == 1 and (r, c) not in visit:
                    unvisit.add((r, c))

        return -1 if unvisit else total
