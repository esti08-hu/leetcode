class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [-1] * len(nums)
        for i, n in enumerate(nums):
            for j in range(i+1, i+l):
                if nums[j%l] > n:
                    res[i] = nums[j%l]
                    break
        return res

