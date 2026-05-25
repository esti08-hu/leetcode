class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        current_sum = 0
        min_prefix_sum = float('inf')
        
        for num in nums:
            current_sum += num
            if current_sum < min_prefix_sum:
                min_prefix_sum = current_sum
        if min_prefix_sum > 0:
            return 1
        
        return 1 - min_prefix_sum