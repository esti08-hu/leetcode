class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        n = len(matrix)
        m = len(matrix[0])

        tran = []

        for j in range(m):
            row = []
            for i in range(n):
                row.append(matrix[i][j])
            tran.append(row)
        return tran