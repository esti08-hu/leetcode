class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n == 0:
            return 0
        elif n%2==1:
            return n*2
        else:
            return n
        
