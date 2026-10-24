class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        nums.sort()
        alice = 0
        for i in range(len(nums)):
            if nums[i] > 9:
                break
            alice += nums[i]

        return alice != sum(nums[i:])