class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        
        def countLessOrEqual(mid):
            
            count = 0
            row = n - 1 
            col = 0
            
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += row + 1 
                    col += 1
                else:
                    row -= 1
            
            return count
        
        left, right = matrix[0][0], matrix[n - 1][n - 1]
        
        while left < right:
            mid = (left + right) // 2
            
            if countLessOrEqual(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        return left