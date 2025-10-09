class Solution:
    def longestPrefix(self, s: str) -> str:
        leg_sub = ""

        for i in range(1, len(s)):
            if s[:i]==s[len(s)-i:]:
                if len(s[:i]) > len(leg_sub):
                    leg_sub = s[:i]
            
        return leg_sub