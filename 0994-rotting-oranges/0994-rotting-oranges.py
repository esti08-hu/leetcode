class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        q = deque()
        time = 0
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((r,c))

        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    
                    if (inbound(row, col) and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh-=1

            time+=1
        return time if fresh == 0 else -1
