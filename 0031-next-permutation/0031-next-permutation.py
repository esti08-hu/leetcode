class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Step 1: Find the breakpoint (rightmost position where nums[i] < nums[i+1])
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # If no breakpoint found, array is in descending order
        # Reverse entire array to get smallest permutation
        if i == -1:
            nums.reverse()
            return
        
        # Step 2: Find the smallest element to the right of breakpoint that's larger than nums[i]
        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        
        # Step 3: Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse everything to the right of position i
        nums[i + 1:] = reversed(nums[i + 1:])