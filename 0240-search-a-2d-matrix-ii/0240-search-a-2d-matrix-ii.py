class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(row):
            low = 0
            high = len(row) - 1

            while low <= high:
                mid = (low + high) // 2

                if row[mid] == target:
                    return True
                
                elif row[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            
        for row in matrix:
            if search(row):
                return True
        return False

