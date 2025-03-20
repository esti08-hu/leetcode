class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        

        def isNice(substing):
            sub_set = set(substing)

            for s in substing:
                if s.swapcase() not in sub_set:
                    return False
            print()
            return True
        
        max_len = float("-inf")
        max_sub = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                sub = s[i:j]
                if isNice(sub):
                    if len(sub) > max_len:
                        max_sub = sub
                        max_len = len(sub)
        
        return max_sub

