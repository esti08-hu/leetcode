class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for i in range(len(arr), 1, -1):
            max_ = max(arr[:i])
            idx_max = arr.index(max_)+1
            
            if idx_max == i:
                continue
            
            if idx_max-1 != 0:
                res.append(idx_max) 
                arr = arr[:idx_max][::-1] + arr[idx_max:]
            
            res.append(i)
            arr = arr[:i][::-1] + arr[i:]

        return res