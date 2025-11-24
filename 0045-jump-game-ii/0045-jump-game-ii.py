class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        if i + nums[i] > n => find min(nums[i:])
        else => find min(nums[i:i+nums[i]])
        
        0  1  2  3  4         
        2  3  1  1  4
        0  0  0  0  0
        '''
        dp = [0]*len(nums)
        n = len(nums)-1
        for i in range(n-1, -1, -1):
            if nums[i] == 0:
                dp[i] = float("inf")
                continue
            curr_jump = i+nums[i]

            if curr_jump > n:
                dp[i] = 1 + min(dp[i+1:])
            else:
                dp[i] = 1 + min(dp[i+1:curr_jump+1])
                
        return dp[0]
