class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        stone_dict = {stones[i]:i for i in range(len(stones))}
        
        cache = {}

        def dfs(k,s):
            if s >= stones[-1]:
                return True
            
            if (k, s) in cache:
                return cache[(k, s)]
            

            for j in range(k-1, k+2):
                if j >0 and j + s in stone_dict:
                    if dfs(j, s+j):
                        cache[(k, s)] = True
                        return True

            cache[(k, s)] = False
            return False

        return dfs(1, 1)