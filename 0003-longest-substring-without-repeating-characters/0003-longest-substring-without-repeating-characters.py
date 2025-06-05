class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            if s[right] in chars:
                left = max(left, chars[s[right]] + 1)
            chars[s[right]] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len