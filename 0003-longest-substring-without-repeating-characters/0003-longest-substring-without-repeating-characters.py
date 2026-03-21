class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        s_set = set()
        ls = 0
        while r < len(s):
            if s[r] in s_set:
                ls = max(ls, len(s_set))
                while s[l] != s[r]:
                    s_set.remove(s[l])
                    l+=1
                l+=1    
            s_set.add(s[r])
            r+=1

        ls = max(ls, len(s_set))
        return ls
