class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res =  0

        for i in range(n):
            for j in range(m):
                row = []
                max_r = 0
                max_c = 0
                r = 0
                while r<n:
                    max_r = max(max_r, grid[r][j])

                    r+=1
                
                c = 0
                while c<m:
                    max_c = max(max_c, grid[i][c])
                    c+=1

                res += (min(max_r, max_c)-grid[i][j])

        return res
