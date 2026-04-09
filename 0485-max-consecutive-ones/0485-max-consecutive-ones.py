class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_1s = 0
        curr = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                max_1s = max(max_1s, curr)
                curr = 0
            else:
                curr += 1
         
        return max(curr, max_1s)