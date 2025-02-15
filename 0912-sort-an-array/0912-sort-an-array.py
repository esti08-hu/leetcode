class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        
        min_val = min(nums)
        max_val = max(nums)
        
        nums_range = max_val - min_val + 1
        count = [0] * nums_range
        
        for n in nums:
            count[n - min_val] += 1
        
        idx = 0
        for i in range(nums_range):
            while count[i] > 0:
                nums[idx] = i + min_val
                count[i] -= 1
                idx += 1
        
        return nums
