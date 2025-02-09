class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for i, n in enumerate(nums):
            dif = target - n
            if dif in prev:
                return [prev [dif], i]
            prev[n] = i
        return