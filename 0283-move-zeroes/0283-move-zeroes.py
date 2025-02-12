class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p_holer = 0

        for seeker in range(len(nums)):
            if nums[seeker] != 0:
                nums[p_holer], nums[seeker] = nums[seeker], nums[p_holer]
                p_holer += 1
