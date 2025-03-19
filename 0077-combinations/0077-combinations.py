class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(s, curr, k1):

            if len(curr) == k1:
                res.append(curr[:])
            
            for i in range(s, n+1):
                curr.append(i)

                backtrack(i+1, curr, k)

                curr.pop()

        backtrack(1, [], k)
        return res