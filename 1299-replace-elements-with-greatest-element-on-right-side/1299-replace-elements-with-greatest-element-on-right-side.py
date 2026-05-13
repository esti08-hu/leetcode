class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1]
        greatest = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            print(arr[i])
            res.append(greatest)
            greatest = max(greatest, arr[i])
        
        return res[::-1]
