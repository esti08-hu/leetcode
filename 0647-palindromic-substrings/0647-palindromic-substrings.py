class Solution:
    def countSubstrings(self, s: str) -> int:
        pal_cnt = 0

        def palCounter(l, r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l-=1
                r+=1
            
            return res

        for i in range(len(s)):
            pal_cnt += palCounter(i, i)
            if i < len(s)-1:
                pal_cnt += palCounter(i, i+1)
        
        return pal_cnt