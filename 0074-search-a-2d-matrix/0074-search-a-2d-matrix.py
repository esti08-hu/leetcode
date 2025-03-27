class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        col = []

        for i in range(n):
            col.append(matrix[i][0])

        idx = bisect_right(col, target)-1
        row = matrix[idx]            

        low, high = 0, len(row)-1

        while low <= high:
            mid = (low+high)//2

            if row[mid] > target:
                high = mid-1
            elif row[mid] < target:
                low = mid +1 
            else: 
                return True
        
        return False


        


