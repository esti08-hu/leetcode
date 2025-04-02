from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()  # Ensure the array is sorted
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > mid:  # Missing number is on the left
                right = mid
            else:  # Missing number is on the right
                left = mid + 1
        return left  # The missing number is at the final position of 'left'