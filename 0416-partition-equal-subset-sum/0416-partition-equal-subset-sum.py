class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False

        target = sum(nums)//2
        cache = {}

        def dfs(i, t):
            if t == target:
                return True
            
            if t > target or i < 0:
                return False
            
            if (i, t) in cache:
                return cache[(i, t)]
            
            inc = dfs(i-1, t+nums[i])
            if inc:
                return True
            exc = dfs(i-1, t)
            if exc:
                return True
            
            cache[(i, t)] = False
            return cache[(i, t)]
        
        return dfs(len(nums)-1, 0)
