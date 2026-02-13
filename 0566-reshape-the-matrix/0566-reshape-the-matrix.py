class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        if rows*cols != r*c:
            return mat

        newMat = [[0]*c for _ in range(r)]

        row, col = 0, 0
        for i in range(rows):
            for j in range(cols):
                if col == c:
                    col = 0
                    row += 1
                    newMat[row][col] = mat[i][j]
                    col += 1
                else:
                    newMat[row][col] = mat[i][j]
                    col += 1
        
        return newMat