class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        i = 0
        while i < len(s):
            if s[i] != t[i]:
                return s[i]
            i += 1

        return t[i]
