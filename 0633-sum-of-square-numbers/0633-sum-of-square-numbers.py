class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sr = math.isqrt(c)
        l,r = 0, sr
        while l <= r:
            curr = l*l + r*r
            if curr > c:
                r-=1
            elif curr < c:
                l+=1
            else:
                return True
        return False