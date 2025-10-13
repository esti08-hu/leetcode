from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        
        n = len(nums)
        max_cache = {}
        min_cache = {}
        
        def max_dp(i):
            if i == 0:
                return nums[0]
            if i in max_cache:
                return max_cache[i]

            prev_max = max_dp(i-1)
            prev_min = min_dp(i-1)
            max_cache[i] = max(nums[i], nums[i] * prev_max, nums[i] * prev_min)
            return max_cache[i]
        
        def min_dp(i):
            if i == 0:
                return nums[0]
            if i in min_cache:
                return min_cache[i]

            prev_max = max_dp(i-1)
            prev_min = min_dp(i-1)
            min_cache[i] = min(nums[i], nums[i] * prev_max, nums[i] * prev_min)
            return min_cache[i]
        
        result = float("-inf")
        for i in range(n):
            result = max(result, max_dp(i))
        
        return result