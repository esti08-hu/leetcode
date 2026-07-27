class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
            
        res = []
        c = 0
        for r in range(m):
            res.append(original[c:c+n])
            c += n
        return res