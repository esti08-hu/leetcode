class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total_elements = m * n
        
        k = k % total_elements
        
        result = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                current_index = i * n + j
                
                new_index = (current_index + k) % total_elements
                
                new_i = new_index // n
                new_j = new_index % n
                
                result[new_i] [new_j] = grid[i][j]
                
        return result