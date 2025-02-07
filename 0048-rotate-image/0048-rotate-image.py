class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        cpy_mat = matrix.copy()
        for c in range(col):
            new_row = []
            for r in range(row):
                new_row.append(cpy_mat[r][c])

            matrix[c] = new_row[::-1]


                



