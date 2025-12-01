# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n

        while r > l:
            m = l + (r - l)//2

            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        
        return l