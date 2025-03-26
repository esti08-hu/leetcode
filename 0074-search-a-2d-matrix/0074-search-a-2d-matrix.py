class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ans = []
        for i in range(len(matrix)):
            ans.extend(matrix[i])

        low, high = 0, len(ans)-1
        while low <= high:
            mid = (low+high)//2
            if ans[mid]>target:
                high = mid -1
            elif ans[mid] < target:
                low = mid+1
            else:
                return True
        
        return False
        


