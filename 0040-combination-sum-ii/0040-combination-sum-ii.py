class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(idx, s, curr_list):
            if s > target:
                return 

            if s == target:
                res.append(curr_list[:])
                return 
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue

                curr_list.append(candidates[i])
                dfs(i+1, s+candidates[i], curr_list)
                curr_list.pop()
            
            return res
        return dfs(0, 0, [])

                