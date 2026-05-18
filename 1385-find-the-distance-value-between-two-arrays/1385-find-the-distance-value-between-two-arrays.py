class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:            
        
        count = 0
        for i in range(len(arr1)):
            for num in arr2:
                if abs(arr1[i] - num) <= d:
                    break
            else:
                count += 1

        return count