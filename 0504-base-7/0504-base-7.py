class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        res = []
        nve = False
        if num < 0:
            nve = True
            num *= -1
            
        while num > 0:
            res.append(str(num%7))
            num//=7
        if nve:
            res.append("-")
        res = res[::-1]
        return "".join(res)