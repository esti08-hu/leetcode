class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        def check(k, nums, queries):
            diff = [0] * len(nums)
            
            for i in range(k):
                l, r, v = queries[i]
                diff[l] += v
                if r + 1 < len(nums):
                    diff[r + 1] -= v
            
            for i in range(1, len(diff)):
                diff[i] += diff[i - 1]
            
            for i in range(len(nums)):
                if nums[i] > diff[i]:
                    return False
            
            return True
        
        num_queries = len(queries)
        
        left, right = 0, num_queries
        ans = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if check(mid, nums, queries):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans 