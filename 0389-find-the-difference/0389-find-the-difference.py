class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        i = 0
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        while i < len(s):
            if s[i] != t[i]:
                return t[i]
            i += 1

        return t[i]
