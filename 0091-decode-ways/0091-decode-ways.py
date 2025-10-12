class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        cache = {}

        def dfs(i):
            if i == len(s):
                return 1

            if s[i] == "0":
                return 0
            
            if i in cache:
                return cache[i]
            
            ways = dfs(i+1)
            if i+1 < len(s) and int(s[i:i+2]) <= 26:
                ways+=dfs(i+2)

            cache[i] = ways

            return cache[i]
        return dfs(0)
        