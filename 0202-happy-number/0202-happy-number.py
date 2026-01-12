class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 10:
            return False
        strt = n
        while True:
            curr = 0
            while n > 0:
                curr += (n%10)**2
                n = n//10
            
            if curr == 1:
                return True
            if curr == strt:
                return False
            n = curr 