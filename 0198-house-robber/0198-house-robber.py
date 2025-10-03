class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==2:
            return max(nums)
        if len(nums)==1:
            return nums[0]

        cache = {}

        def dfs(i):
            if i == len(nums)-1:
                return nums[i]
            
            if i in cache:
                return cache[i]
            
            curr = nums[i]
            res = [0]
            for j in range(i+2, len(nums)):
                res.append(dfs(j))
            curr+=max(res)

            cache[i] = curr
            return curr
        
        ans = 0
        for i in range(len(nums)):
            ans = max(ans, dfs(i))
        return ans
