class Solution:
    def minimumLength(self, s: str) -> int:
        while len(s) > 1 and s[0] == s[-1]:
            c = s[0]
            s = s.strip(c)
        return len(s)
