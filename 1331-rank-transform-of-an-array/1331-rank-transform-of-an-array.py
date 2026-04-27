class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        res = []
        sorted_arr = sorted(arr)

        arr_map = {}
        j = 1
        for v in sorted_arr:
            if v not in arr_map:
                arr_map[v] = j
                j+=1
        
        for v in arr:
            res.append(arr_map[v])
        
        return res
