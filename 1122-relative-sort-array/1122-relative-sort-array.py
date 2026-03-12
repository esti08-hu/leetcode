class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_counter = Counter(arr1)
        res = []
        print(arr1_counter[2])
        for i in range(len(arr2)):
            if arr2[i] in arr1_counter:
                v = arr1_counter[arr2[i]]
                for j in range(v):
                    res.append(arr2[i])
                    arr1_counter[arr2[i]] -= 1
                if arr1_counter[arr2[i]] == 0:
                    del arr1_counter[arr2[i]]

        
        for k in sorted(arr1_counter.keys()):
            for i in range(arr1_counter[k]):
                res.append(k)
    
        return res