class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1), 
                      (1,1), (1,-1), (-1,1), (-1,-1)]
        
        n = len(grid)
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        q = deque([(0, 0, 1)])
        
        visited = set([(0,0)])
        
        while q:
            i,j,steps = q.popleft()
            if i == n-1 and j == n-1:
                return steps
            
            for di, dj in directions:
                ni, nj = i+di, j+dj
                
                if 0<=ni<n and 0<=nj<n and grid[ni][nj] == 0 and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    q.append((ni, nj, steps + 1))
        return -1