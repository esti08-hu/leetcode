class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest = 1
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr+=1
            else:
                longest = max(longest, curr)
                curr = 1
        
        return max(longest, curr)

