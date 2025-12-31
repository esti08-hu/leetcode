class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        l           r
        1 2 1 3 5 6 4
        if l > l+1: 
            return l
        if r > r - 1:
            return r

        while l < r:
            if l > l+1:
                l+=2
            elif r > r - 1:
                r -= 2
            elif l < l+1:
                l = l+1
            elif r < r -1:
                r -= 1
        '''
        if len(nums) == 1:
            return 0
        l, r = 0, len(nums) - 1

        if nums[l] > nums[l + 1]:
            return l
        elif nums[r] > nums[r-1]:
            return r
        
        while l < r:
            if nums[l] > nums[l+1]:
                l += 2
            elif nums[l] < nums[l+1]:
                if nums[l+1] > nums[l+2]:
                    return l + 1
                l += 1
            
            if nums[r] > nums[r-1]:
                r -= 2
            elif nums[r] < nums[r-1]:
                if nums[r-1] > nums[r-2]:
                    return r-1
                r -= 1
        

                