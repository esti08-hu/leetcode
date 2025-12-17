class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = float("-inf")
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                max_sum = max(max_sum, curr_sum)
                curr_sum = nums[i]
                continue
            curr_sum+=nums[i]
            
        return max(curr_sum, max_sum)