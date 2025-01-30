class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.split()
        s="".join(s)
        res=""
        c="q11w"
        print(c[1].isnumeric())
        for c in s:
            if not c.isupper() or not c.islower() and c.isnumeric():
                continue
            else: 
                res+=c
                continue
        res_lower= res.lower()
        return res_lower == res_lower[::-1]
