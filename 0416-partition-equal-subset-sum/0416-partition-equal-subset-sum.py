class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False

        target = sum(nums)//2
        cache = {}

        def dfs(i, t):
            if t == 0:
                return True
            
            if t < 0 or i == len(nums):
                return False
            
            if (i, t) in cache:
                return cache[(i, t)]
            
            inc = dfs(i+1, t-nums[i])
            if inc:
                return True
            exc = dfs(i+1, t)
            
            cache[(i, t)] = inc or exc
            return cache[(i, t)]
        
        return dfs(0, target)
