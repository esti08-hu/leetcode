class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left = 0 
        right = 1
        zeros = []
        while left < right and right < len(nums):
            if nums[left] != 0 and nums[left] == nums[right]:
                nums[left] *= 2
                nums[right] = 0
                left += 1
                right += 1
            right += 1
            left += 1

        non_zeros = [num for num in nums if num != 0]
        zero_count = len(nums) - len(non_zeros)
        nums = non_zeros + [0] * zero_count
        
        return nums