class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        ans = symbols[s[-1]]
        for i in range(1,len(s)):
            if symbols[s[i-1]] < symbols[s[i]]:
                ans -= symbols[s[i-1]]
            else:
                ans += symbols[s[i-1]]
        
        return ans
        