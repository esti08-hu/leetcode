class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        s = 0
        for d in str(n):
            p*=int(d)
            s+=int(d)
        
        return p - s
