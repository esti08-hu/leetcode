class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums_hash = {}

        for i in range(len(nums)):
            if nums[i] not in nums_hash:
                nums_hash[nums[i]] = 1
            else:
                nums_hash[nums[i]] += 1
            
            if nums_hash[nums[i]] > 1:
                return nums[i]
            