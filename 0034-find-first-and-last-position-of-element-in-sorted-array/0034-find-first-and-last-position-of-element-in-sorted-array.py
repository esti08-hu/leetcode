from bisect import bisect_left, bisect_right
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def firstOccerence(nums, target):
            idx = bisect_left(nums, target)
            if idx < len(nums) and nums[idx] == target:
                return idx
            return -1

        
        def lastOccerence(nums, target):
            idx = bisect_right(nums, target) -1 
            if idx >= 0 and nums[idx] == target:
                return idx
            return -1
        

        return [firstOccerence(nums, target), lastOccerence(nums, target)]
                