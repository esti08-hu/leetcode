class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums.append(0)
        max_1 = 0
        count = 0
        for i in range(len(nums)):
            if nums[i]:
                count += 1
            else:
                max_1 = max(max_1, count)
                count = 0

        return max_1