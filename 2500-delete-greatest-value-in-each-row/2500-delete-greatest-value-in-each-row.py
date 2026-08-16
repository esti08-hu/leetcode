class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res = 0

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            grid[r].sort(reverse=True)
        
        for c in range(cols):
            curr_max = 0
            for r in range(rows):
                curr_max = max(curr_max, grid[r][c])
            
            res  += curr_max

        return res
