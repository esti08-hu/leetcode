class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max = 0
        global_max = nums[0]

        curr_min = 0
        global_min = nums[0]
        total_sum = 0
        for x in nums:
            curr_max = max(x, curr_max+x)
            global_max = max(global_max, curr_max)

            curr_min = min(x, curr_min+x)
            global_min = min(global_min, curr_min)

            total_sum += x
        
        if global_max < 0:
            return global_max
        
        return max(global_max, total_sum - global_min)