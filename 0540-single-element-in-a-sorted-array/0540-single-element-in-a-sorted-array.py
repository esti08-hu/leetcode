class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        low = 0
        high = len(nums)-1
        ans  = -1

        while low < high:
        
            mid = (low + high) // 2

            if mid%2:
                mid -= 1
            
            if  nums[mid] == nums[mid+1]:
                low = mid + 2
            else:
                high = mid 
        return nums[low]
        