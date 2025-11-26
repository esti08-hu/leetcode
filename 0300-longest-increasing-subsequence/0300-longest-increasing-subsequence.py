class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[-1] = 1

        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                dp[i] = 1 + dp[i+1]  
            else:
                dp[i] = dp[i+1]
        return dp[0]