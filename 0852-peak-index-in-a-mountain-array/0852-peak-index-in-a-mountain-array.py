class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr)-1

        while left < right:
            mid = (left + right) >> 1
            if arr[mid+1] < arr[mid]:
                right = mid
            else:
                left = mid + 1
        
        return left