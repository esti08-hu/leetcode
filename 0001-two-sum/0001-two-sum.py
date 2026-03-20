class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            if target - nums[i] not in hashMap:
                hashMap[nums[i]] = i
            else:
                return [hashMap[target - nums[i]], i]