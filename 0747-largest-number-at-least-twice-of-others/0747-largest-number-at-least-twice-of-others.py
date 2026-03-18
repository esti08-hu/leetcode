class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_val = max(nums)
        idx = -1

        for i in range(len(nums)):
            if nums[i] == max_val:
                idx = i
                continue
            if nums[i] * 2 > max_val:
                return -1
        return idx
