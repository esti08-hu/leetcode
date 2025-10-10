class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache

        def dp(i, t):
            if i >= len(nums) or t < 0:
                return 0
            
            if t == 0:
                return 1
            
            curr = 0 
            for j in range(len(nums)):
                curr+=dp(j, t - nums[j])
            
            return curr
        
        return dp(0, target)

                