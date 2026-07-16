class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prev:
                res += 1
                prev += 1
            elif nums[i] < prev:
                res += (prev - nums[i] + 1)
                prev = nums[i] + (prev - nums[i] + 1)
            else:
                prev = nums[i]
        
        return res
