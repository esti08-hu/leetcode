class Solution:
    def findComplement(self, num: int) -> int:
        def numToBit(n):
            res = []

            while n > 0:
                res.append(n%2)
                n//=2
            return res
        
        def comp(b):
            for i in range(len(b)):
                if b[i]:
                    b[i] = 0
                else:
                    b[i] = 1
            return b
        
        def bitToNum(b):
            total = 0
            for i in range(len(b)):
                if b[i]:
                    total += (2**i)
            
            return total
        
        return bitToNum(comp(numToBit(num)))
