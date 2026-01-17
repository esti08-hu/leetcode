class Solution:
    def reverseBits(self, n: int) -> int:
        def convertInt(n):
            res = [0] * 32
            i = 0
            while n > 0:
                if n%2:
                    res[i] = 1
                i += 1
                n//=2
            return res[::-1]
        def convertBit(b):
            res = 0
            i = 0
            for i in range(32):
                if b[i]:
                    res += 2**i
            return res

        return convertBit(convertInt(n))
