class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        for si in s:
            si = list(si)

        res = []

        for si in s:
            res.append("".join(si[::-1]))
        
        return " ".join(res)

        
        