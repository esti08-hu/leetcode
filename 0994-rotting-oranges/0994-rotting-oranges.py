class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid) 
        cols = len(grid[0])

        def inBound(r,c):
            return(0<=r<rows and 0<=c<cols)

        fresh = 0
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        time = 0
        while q and fresh > 0:
            len_q =  len(q)

            for _ in range(len_q):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr,nc = r+dr, c+dc

                    if inBound(nr, nc):
                        if grid[nr][nc] == 1:
                            grid[nr][nc]=2
                            fresh-=1
                            q.append((nr, nc))
            time +=1
        
        return time if fresh==0 else -1








