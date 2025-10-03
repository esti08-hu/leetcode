class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        @cache
        def dfs(i, end):
            if i>= end:
                return 0
            
            rob = nums[i] + dfs(i+2, end)
            skip = dfs(i+1, end)
        
            return max(rob, skip)
        return max(dfs(0, len(nums)-1), dfs(1, len(nums)))