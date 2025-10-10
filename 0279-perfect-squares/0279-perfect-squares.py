class Solution:
    @cache
    def numSquares(self, n: int) -> int:
        
        if n == 0:
            return 0
        
        if 1 <= n <= 3:
            return n
        
        max_sqr = int(math.sqrt(n))
        curr = float("inf")
        for i in range(max_sqr, 0, -1):
            if n >= i**2:
                curr = min(curr, 1+self.numSquares(n-i**2))

        return curr