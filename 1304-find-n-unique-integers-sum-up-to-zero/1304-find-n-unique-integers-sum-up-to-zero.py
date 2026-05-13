class Solution:
    def sumZero(self, n: int) -> List[int]:
        target = ((n-1)*(n)) // 2

        res = [-1 * target]

        for i in range(1, n):
            res.append(i)
        
        return res
