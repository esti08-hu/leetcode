class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        8 
        0 1 2 3 4 5 6 7 8
        '''
        l, r = 0, x

        while l < r-1:
            mid = (l + r) >> 1
            sroot = mid * mid
            if sroot == x:
                return mid
            elif sroot > x:
                r = mid
            else:
                l = mid
        
        return r if r*r <= x else l