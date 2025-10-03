class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def dfs(i):
            if i>=len(nums):
                return 0
            
            rob = nums[i]+dfs(i+2)
            skip = dfs(i+1)

            return max(rob, skip)
        
        return dfs(0)