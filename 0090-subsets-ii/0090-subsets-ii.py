class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(idx, curr_set):
            res.append(curr_set[:])
            
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                
                curr_set.append(nums[i])
                dfs(i+1, curr_set)
                curr_set.pop()
            return res
            
        return dfs(0, [])
