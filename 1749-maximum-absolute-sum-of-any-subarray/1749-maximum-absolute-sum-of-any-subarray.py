class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_min = 0
        curr_max = 0
        max_sum = 0
        min_sum = 0
        for num in nums:
            curr_max += num
            if curr_max < 0:
                curr_max = 0
            max_sum = max(curr_max, max_sum)

            curr_min += num
            if curr_min > 0:
                curr_min = 0
            min_sum = min(curr_min, min_sum)
        
        return max(max_sum, abs(min_sum))