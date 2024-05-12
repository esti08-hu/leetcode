class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(1, n - 1):
            for j in range(1, n - 1):
                temp = max([grid[k][l] for k in range(i - 1, i + 2) for l in range(j - 1, j + 2)])
                res[i - 1][j - 1] = temp

        return res