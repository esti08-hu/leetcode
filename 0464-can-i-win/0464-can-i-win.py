class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        cache = {}
        if (maxChoosableInteger*(maxChoosableInteger+1))//2 < desiredTotal:
            return False
        
        def dfs(used_set, total):
            key = tuple(sorted(used_set))
            if key in cache:
                return cache[key]

            for i in range(1, maxChoosableInteger + 1):
                if i not in used_set:
                    if i >= total:
                        cache[key] = True
                        return True

                    next_used = used_set | {i}
                    if not dfs(next_used, total-i):
                        cache[key] = True
                        return True

            cache[key] = False 
            return False

        return dfs(set(), desiredTotal)