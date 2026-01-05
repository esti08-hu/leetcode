class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        N= len(grid)
        pq = [(grid[0][0], 0, 0)]
        
        visited = set()
        visited.add((0, 0))
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while pq:
            current_height, r, c = heapq.heappop(pq)
        
            if r == N - 1 and c == N - 1:
                return current_height
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    new_height = max(current_height, grid[nr][nc])
                    heapq.heappush(pq, (new_height, nr, nc))
        return -1
            