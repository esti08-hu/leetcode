class Solution:
    def climbStairs(self, n: int) -> int:
        res = [1, 2]
        if n <= 2:
            return res[n-1]
        
        for i in range(n-2):
            temp = res[1]
            res[1] = sum(res)
            res[0] = temp
        
        return res[1]