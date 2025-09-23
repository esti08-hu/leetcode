class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(idx):
            if idx >= len(nums):
                return 0
            
            if idx in memo:
                return memo[idx]

            r = nums[idx] + dfs(idx + 2)
            skip = dfs(idx+1)

            memo[idx] = max(r, skip)

            return memo[idx]
        return dfs(0)

            
    
    


