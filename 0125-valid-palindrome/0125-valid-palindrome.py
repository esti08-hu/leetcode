class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        for c in s:
            if not c.isupper() and not c.islower() and not c.isnumeric():
                continue
            else: 
                res+=c
        res_lower= res.lower()
        return res_lower == res_lower[::-1]
