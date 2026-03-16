class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc  = False
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc = True
            if nums[i] < nums[i-1]:
                break
        
        if inc:
            for i in range(1, len(nums)):
                if nums[i] < nums[i-1]:
                    return False
        else:
            for i in range(1, len(nums)):
                if nums[i] > nums[i-1]:
                    return False
        
        return True