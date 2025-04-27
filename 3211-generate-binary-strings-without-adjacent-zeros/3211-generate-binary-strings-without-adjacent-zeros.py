class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        
        def dfs(curr, n):
            if len(curr) == n:
                res.append(curr)
                return
            for i in range(2):
                if i == 0 and curr and curr[-1] == "0":
                    continue
                dfs(curr + str(i), n)
                
        dfs("", n)
        return res