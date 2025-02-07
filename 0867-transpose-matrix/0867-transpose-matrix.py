class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        col = len(matrix)
        row = len(matrix[0])
        
        transposed = []
        for c in range(row):
            new_row = []
            for r in range(col):
                new_row.append((matrix[r][c]))
            transposed.append(new_row)

        return transposed