class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        res = [0] * len(nums)
        i = len(nums) - 1
        
        while l <= r:
            if nums[r]*nums[r] >= nums[l] * nums[l]:
                res[i] = nums[r]*nums[r]
                i-=1
                r-=1
            else:
                res[i] = nums[l]*nums[l]
                i -= 1
                l += 1
        
        return res