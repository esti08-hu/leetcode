class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        1 2 3
        8 9 4
        7 6 5

        val = 9
        i, j = 1, 1
        while val <= n*n:
            # right 
            while j+1 < n and mat[i][j+1] == 0:
                mat[i][j+1] = val
                val += 1
                j+=1
            # down
            while i+1 < n and mat[i+1][j] == 0:
                mat[i+1][j] = val
                val += 1
                i+=1
            # left
            while j-1 >= 0 and mat[i][j-1] == 0:
                mat[i][j-1] = val
                val += 1
                j -= 1
            # up
            while i-1 >= 0 and mat[i-1][j] == 0:
                mat[i-1][j] = val
                val += 1
                i -= 1
        """
        mat = [[0]*n for _ in range(n)]
        mat[0][0] = 1
        val = 2
        i, j = 0, 0
        while val <= n*n:
            # right 
            while j+1 < n and mat[i][j+1] == 0:
                mat[i][j+1] = val
                val += 1
                j+=1
            # down
            while i+1 < n and mat[i+1][j] == 0:
                mat[i+1][j] = val
                val += 1
                i+=1
            # left
            while j-1 >= 0 and mat[i][j-1] == 0:
                mat[i][j-1] = val
                val += 1
                j -= 1
            # up
            while i-1 >= 0 and mat[i-1][j] == 0:
                mat[i-1][j] = val
                val += 1
                i -= 1
        
        return mat