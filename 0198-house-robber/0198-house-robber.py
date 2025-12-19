class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dfs(idx):
            if idx >= len(nums):
                return 0
            
            rob = nums[idx] + dfs(idx+2)
            skip = dfs(idx+1)

            return max(rob, skip)
        
        return dfs(0)