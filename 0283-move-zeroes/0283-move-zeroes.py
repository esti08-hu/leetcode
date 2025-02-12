class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p_holder = 0
        seeker = 0
        # for seeker in range(len(nums)):
        while seeker < len(nums):
            if nums[seeker] != 0:
                nums[p_holder], nums[seeker] = nums[seeker], nums[p_holder]
                p_holder += 1
            
            seeker += 1