class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c ==0:
            return True
        for i in range(1, int(math.sqrt(c))+1):
            a = math.pow(i,2)
            b = int(c - a)

            if b == math.pow(math.sqrt(b), 2):
                return True
        
        return False 