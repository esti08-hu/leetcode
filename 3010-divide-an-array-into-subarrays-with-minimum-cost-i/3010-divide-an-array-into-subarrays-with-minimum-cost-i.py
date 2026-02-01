class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        res = [nums[0]]
        nums = sorted(nums[1:])

        res += nums[:2]

        return sum(res)
