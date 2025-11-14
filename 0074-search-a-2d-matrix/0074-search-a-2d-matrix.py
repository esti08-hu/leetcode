class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        row = 0 col = 3
        if (0, 3) < target:
            row += 1
        if (row, col) > taret:
            row-=1
        else:
            return True
        """

        row, col = len(matrix), len(matrix[0])
        r, c = 0, col-1

        while r < row and c >= 0:
            if matrix[r][c] < target:
                r+=1
            elif matrix[r][c] > target:
                c-=1
            else:
                return True
        
        return False
