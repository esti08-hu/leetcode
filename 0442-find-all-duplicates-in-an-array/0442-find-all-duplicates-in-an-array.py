from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        # left, right = 1, len(nums)
        # print(nums)
        res = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                res.append(nums[i])
        return res