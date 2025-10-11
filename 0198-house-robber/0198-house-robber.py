class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def dp(i):
            if i < 0:
                return 0
            
            if i in cache:
                return cache[i]
            
            rob = nums[i] + dp(i-2)
            skip = dp(i-1)
            cache[i] = max(rob, skip)
            
            return cache[i]
        
        return dp(len(nums)-1)
    
   