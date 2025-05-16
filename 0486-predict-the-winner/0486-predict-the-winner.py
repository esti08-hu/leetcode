class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(nums, l, r):
            if l == r:
                return nums[l]
            left = nums[l] - helper(nums, l + 1, r)
            right = nums[r] - helper(nums, l, r - 1)
            return max(left, right)
        
        return helper(nums, 0, len(nums) - 1) >= 0
         