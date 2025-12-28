class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        m = 2
        n = 3
        low = [0, 0]
        high = [2, 3]

        mid = [1, 1]
        00 - 34
        1+3//2
        4+1//2
        22
        high = (pr, pc-1)

        00 - 21
        11

        total = 12
        6 
        6//cols = cur_row
        6%cols = cur_col

        22
        2*cols + cur_col = 6

        '''

        rows, cols = len(matrix), len(matrix[0])

        total = rows * cols
        high = total - 1
        low = 0
        while low <= high:
            mid = (low + high) // 2
            cur_row = mid//cols
            cur_col = mid%cols

            if matrix[cur_row][cur_col] == target:
                return True
            elif matrix[cur_row][cur_col] > target:
                high = mid - 1
            else:
                low = mid + 1

        return False
