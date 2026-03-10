class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid)
        total = 0

        for r in range(rows):
            for c in range(cols):
                v = grid[r] [c]
                if v > 0:
                    total += 2 + 4 * v  # top + bottom + 4 sides

                # Subtract overlap with the cell above
                if r > 0:
                    total -= 2 * min(v, grid[r-1] [c])

                # Subtract overlap with the cell to the left
                if c > 0:
                    total -= 2 * min(v, grid[r] [c-1])

        return total