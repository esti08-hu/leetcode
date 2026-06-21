class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr_set = set(arr)
        total = len(arr) + k
        count = 0
        for i in range(1, total + 1):
            if i not in arr_set:
                count += 1
            
            if count == k:
                return i
        