class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(curr, x):
            if len(curr) == k:
                res.append(curr[:])
                return 
            
            if  x > k-len(curr):
                backtrack(curr, x-1)
            
            curr.append(x)
            backtrack(curr, x-1)
            curr.pop()
        
        backtrack([], n)
        return res
