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
            
            curr = nums[i]
            res = [0]
            for j in range(i+2, n):
                res.append(dfs(j, n))
            curr+=max(res)

            cache[(i, n)] = curr
            return curr
        
        ans = 0
        n = len(nums)
        for i in range(len(nums)):
            if i == 0:
                ans = max(ans, dfs(i, n-1))
            else:
                ans = max(ans, dfs(i, n))
        return ans
