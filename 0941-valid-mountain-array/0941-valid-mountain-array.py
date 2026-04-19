class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        I = False
        D = False

        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                return False
            if arr[i] > arr[i-1]:
                if D:
                    return False
                I = True
            if arr[i] < arr[i-1]:
                D = True

        return I and D