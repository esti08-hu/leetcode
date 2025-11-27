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
            
            num_set = set()

            for i in range(idx, len(candidates)):
                if candidates[i] in num_set:
                    continue

                num_set.add(candidates[i])
                curr_list.append(candidates[i])
                dfs(i+1, s+candidates[i], curr_list)
                curr_list.pop()
            
            return res
        return dfs(0, 0, [])

                