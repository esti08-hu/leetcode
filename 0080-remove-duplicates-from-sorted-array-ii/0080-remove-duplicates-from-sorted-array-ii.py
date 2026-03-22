class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        write = 2  # Start writing from index 2
        for read in range(2, len(nums)):
            if nums[read] != nums[write - 2]:  # Allow at most 2 of same number
                nums[write] = nums[read]
                write += 1
        return write