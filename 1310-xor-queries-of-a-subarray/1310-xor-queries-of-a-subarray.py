class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pref = [arr[0]]
        for i in range(1, len(arr)):
            pref.append(arr[i] ^ pref[i-1])
        
        res = []
        for l, r in queries:
            if l == 0:
                res.append(pref[r])
            else:
                res.append(pref[r] ^ pref[l-1])
        return res