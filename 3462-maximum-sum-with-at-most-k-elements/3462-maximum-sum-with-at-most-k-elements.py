class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heap = []
        n = len(grid)
        m = len(grid[0])
        
        for i in range(n):
            limit = limits[i]
            row_heap = []
            
            for j in range(m):
                heappush(row_heap, grid[i][j])
                if len(row_heap) > limit:
                    heappop(row_heap) 
            
            for val in row_heap:
                heappush(heap, val)
                if len(heap) > k:
                    heappop(heap)
                    
        return sum(heap)