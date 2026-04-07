class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        mat = [[0]*n for _ in range(m)]
        odd = 0
        for r, c in indices:
            for i in range(n):
                mat[r][i] += 1
                if mat[r][i] % 2:
                    odd += 1   
                else:
                    odd -= 1

            for j in range(m):
                mat[j][c] += 1
                if mat[j][c] % 2:
                    odd += 1
                else:
                    odd -= 1
            
        return odd