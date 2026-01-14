class Solution:
    def countArrangement(self, n: int) -> int:
        self.count = 0
        self.seen = set()
        def dfs(idx, perm):
            if len(perm) == n:
                self.count += 1
                return 
            
            for i in range(1, n+1):
                if (not perm or (not ((len(perm)+1)%(i)) or not ((i)%(len(perm)+1)))) and i not in self.seen :
                    perm.append(i)
                    self.seen.add(i)
                    dfs(i+1, perm)
                    self.seen.remove(i)
                    perm.pop()
        
        dfs(0, [])
        return self.count
