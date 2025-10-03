class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==2:
            return max(nums)
        if len(nums)==1:
            return nums[0]

        cache = {}

        def dfs(i, n):
            if i >= n:
                return 0

            if (i,n) in cache:
                return cache[(i,n)]
            
            rob = nums[i] + dfs(i+2, n)
            skip = dfs(i+1, n)
            cache[(i, n)] = max(rob, skip)
            return cache[(i, n)]
        
        ans = 0
        n = len(nums)
        ans = max(ans, dfs(0, n-1))
        ans = max(ans, dfs(1, n))
        return ans
