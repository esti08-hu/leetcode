class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        original_sum = sum([i for i in range(len(nums)+1)])
        nums_sum = sum([i for i in (nums)])
        return original_sum - nums_sum