class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache

        def dfs(i, j):
            n = len(triangle)
            if i>=n or j>=n:
                return 0
            
            m1 = triangle[i][j] + dfs(i+1, j)
            m2 = triangle[i][j] + dfs(i+1, j+1)

            return min(m1, m2)
        
        return dfs(0,0)
            
            