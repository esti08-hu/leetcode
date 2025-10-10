class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.max_pal = ""
        self.pal_len = 0
        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r -l +1) > self.pal_len:
                    self.max_pal = s[l:r+1]
                    self.pal_len = r -l + 1
                l -= 1
                r += 1
            return self.max_pal
        
        for i in range(len(s)):
            helper(i, i)  # odd length palindromes
            if i < len(s) - 1:
                helper(i, i + 1)  # even length palindromes
        
        return self.max_pal