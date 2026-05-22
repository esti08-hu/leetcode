class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = 0
        j = 0
        for i in range(len(num1)-1, -1, -1):
            n1 += 10**j * int(num1[i])
            j+=1

        n2 = 0
        j = 0
        for i in range(len(num2)-1, -1, -1):
            n2 += 10**j * int(num2[i])
            j+=1
        
        total = n1 + n2
        if total <= 9:
            return str(total)
            
        res = []
        while total > 0:
            res.append(str(total%10))
            total //= 10
        
        return "".join(res[::-1])