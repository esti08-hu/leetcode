class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] < 0:
                    count += 1
        return count