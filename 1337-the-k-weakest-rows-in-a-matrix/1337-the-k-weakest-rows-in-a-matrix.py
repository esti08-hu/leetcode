class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Create list of (soldier_count, row_index)
        rows = [(sum(row), i) for i, row in enumerate(mat)]
        # Sort by soldier count, then by row index
        rows.sort(key=lambda x: (x, x))
        # Return first k row indices
        return [row[1] for row in rows[:k]]