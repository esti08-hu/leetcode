class Solution:
    def shortestPalindrome(self, s: str) -> str:
        i = len(s)-1
        lg = ""
        s = list(s)
        while i >= 0:
            if s[i] == s[0]:                
                if s[:i+1] == s[:i+1][::-1]:
                    lg = s[:i+1]
                    break
            i-=1
        res = []
        res = s[len(lg):][::-1] + s
        return "".join(res)