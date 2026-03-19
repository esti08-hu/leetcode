class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_dist = float("inf")

        for i in range(1, len(arr)):
            min_dist = min(min_dist, arr[i] - arr[i-1])

        res = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == min_dist:
                res.append([arr[i-1], arr[i]])
        
        return res
