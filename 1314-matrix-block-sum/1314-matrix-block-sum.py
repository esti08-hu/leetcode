class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n,m = len(mat), len(mat[0])

        prefix = [[0]*(m+1) for _ in range(n+1)]
        res = []
        for i in range(n):
            for j in range(m):
                prefix[i+1][j+1] = prefix[i+1][j] + prefix[i][j+1] - prefix[i][j] + mat[i][j]

        for i in range(n):
            row = []
            for j in range(m):
                r1 = max(0, i-k)
                c1 = max(0, j-k)

                r2 = min(n-1, i+k)
                c2 = min(m-1, j+k)

                val = prefix[r2+1][c2+1] - prefix[r2+1][c1] - prefix[r1][c2+1] + prefix[r1][c1]

                row.append(val)
            res.append(row)

        return res
