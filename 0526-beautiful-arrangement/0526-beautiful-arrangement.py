class Solution:
    def countArrangement(self, n: int) -> int:
        self.count = 0
        self.seen = set()
        # @cache
        def dfs(perm):
            if len(perm) == n:
                self.count += 1
                return 
            
            for i in range(1, n+1):
                pos = len(perm) + 1
                if (not perm or (pos % i == 0 or i % pos == 0)) and i not in self.seen:               
                    perm.append(i)
                    self.seen.add(i)
                    dfs(perm)
                    self.seen.remove(i)
                    perm.pop()
        
        dfs([])
        return self.count
