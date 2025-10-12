class Solution:
    def countSubstrings(self, s: str) -> int:
        self.pal_cnt = 0

        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.pal_cnt += 1
                l-=1
                r+=1
            
            return 
        
        for i in range(len(s)):
            helper(i, i)
            if i < len(s)-1:
                helper(i, i+1)
        
        return self.pal_cnt