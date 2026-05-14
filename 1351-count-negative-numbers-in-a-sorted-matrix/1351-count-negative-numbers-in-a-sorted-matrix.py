class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        count = 0
        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if grid[r][c] < 0:
                    count += 1
                elif grid[r][c] >= 0:
                    break
        return count