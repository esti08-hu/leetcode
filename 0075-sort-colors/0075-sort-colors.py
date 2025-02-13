class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0]*3
        for n in nums:
            count[n] +=1

        index = 0
        for c in range(len(count)):
            for i in range(count[c]):
                nums[index] = c
                index += 1