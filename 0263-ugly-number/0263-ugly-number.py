class Solution:
    def isUgly(self, n: int) -> bool:
        '''
        {2,3,5}
        14 => 1 2 7

        '''
        if n <= 0:
            return False
            
        prime = {2, 3, 5}
        d = 2
        while d * d <= n:
            while n % d == 0:
                if d not in prime:
                    return False
                n //= d
            d += 1
        if n > 1:
            if n not in prime:
                    return False
        return True
                
