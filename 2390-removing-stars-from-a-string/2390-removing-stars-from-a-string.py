class Solution:
    def removeStars(self, s: str) -> str:
        stk = []
        for c in s:
            if c == "*" and stk:
                stk.pop()
            else:
                stk.append(c)
        return "".join(map(str, stk))