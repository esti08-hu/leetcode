class Solution:
    def longestOnes(self, nums, k):
        left, maxLength, zero_count  = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count  += 1
            while zero_count  > k:
                if nums[left] == 0:
                    zero_count  -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength
