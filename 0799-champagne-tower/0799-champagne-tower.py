class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        @cache

        def dfs(r, c):
            if r < 0 or c < 0 or c > r:
                return 0
            if r == 0 and c == 0:
                return poured
            
            left = dfs(r-1, c-1)
            right = dfs(r-1, c)
            
            left_overflow = max(0, left-1)
            right_overflow = max(0, right-1)
            return max((left_overflow + right_overflow)/2, 0)
        res = dfs(query_row, query_glass)
        return 1 if res > 1 else res