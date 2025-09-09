class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        num_to_idx = {}

        for i, num in enumerate(nums):
            exists = target-num
            if exists in num_to_idx:
                return [num_to_idx[exists], i]
            num_to_idx[num] = i