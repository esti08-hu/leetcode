class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        res = 0
        # Main diagonal
        for i in range(n):
            res += mat[i][i]
        
        # Secondary diagonal
        i = 0
        for j in range(n - 1, -1, -1):
            res += mat[i][j]
            i+=1
        # Odd len matrix adds the middle val twice 
        if n%2:
            pos = n//2
            res -= mat[pos][pos]
        
        return res
