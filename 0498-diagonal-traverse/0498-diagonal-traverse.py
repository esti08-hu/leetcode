class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
            if not mat:
                return []
            
            rows, cols = len(mat), len(mat[0])
            result = []
            
            for diagonal in range(rows + cols - 1):
                if diagonal < cols:
                    i = 0
                    j = diagonal
                else:
                    i = diagonal - cols + 1
                    j = cols - 1

                diagonal_elements = []
                while i < rows and j >= 0:
                    diagonal_elements.append(mat[i][j])
                    i += 1
                    j -= 1
                
                if (diagonal + 1) % 2 == 0:
                    result.extend(diagonal_elements)
                else:
                    result.extend(diagonal_elements[::-1])
            
            return result