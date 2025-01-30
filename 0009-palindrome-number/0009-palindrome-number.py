class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = 0
        y = x
        l = len(str(x))
        for i in range(l):
            r = x % 10
            a = x//10
            x = a
            dig = 10**(l-i-1)
            ans += (dig*r)
        if (y == ans):
            return True
        else:
            return False
        return False