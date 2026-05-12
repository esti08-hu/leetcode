class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        arr_cnt = Counter(arr)

        target = len(arr)//4 + 1

        for k, v in arr_cnt.items():
            if v >= target:
                return k
            