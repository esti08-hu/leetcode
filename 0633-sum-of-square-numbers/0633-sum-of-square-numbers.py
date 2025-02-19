class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 0:
            return False
        for i in range(int(math.sqrt(c))+1):
            a = math.pow(i,2)
            b = int(c - a)
            if b < 0:
                continue 

            if b == math.pow(int(math.sqrt(b)), 2):
                return True
        
        return False 