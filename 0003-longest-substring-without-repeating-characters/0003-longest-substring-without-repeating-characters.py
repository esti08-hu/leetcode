class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        |  |
        abcabcbb
        ||
        bbbbb
        '''
        l, r = 0, 0
        max_sub = 0
        s_set = set()
        while l <= r and r < len(s):
            
            while s[r] in s_set:
                s_set.remove(s[l])
                l+=1
            s_set.add(s[r])
            r+=1

            if l == r:
                r += 1
            
            max_sub = max(max_sub, len(s_set))
        
        return max_sub