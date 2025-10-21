class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
            
        def dp1(nums):
            dp = [nums[-2],nums[-1]]
            for i in range(len(nums)-3, -1, -1):
                tmp = dp[0]
                if dp[0]-nums[i+1] > dp[1]:
                    dp[0] = dp[0]-nums[i+1]+nums[i]
                else:
                    dp[0] = dp[1] + nums[i]
                dp[1]=tmp
            
            return max(dp)

        
        return max(dp1(nums[:-1]), dp1(nums[1:]))
         
