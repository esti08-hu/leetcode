class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(prev, num_set, total):
            if len(num_set) == k:
                if total == n:
                    curr = list(num_set)
                    res.append(curr[::])
                return
            
            for num in range(prev + 1, 10):
                if total + num > n:
                    return

                num_set.add(num)
                dfs(num, num_set, total + num)
                num_set.remove(num)
        
        dfs(0, set(), 0)
        return res