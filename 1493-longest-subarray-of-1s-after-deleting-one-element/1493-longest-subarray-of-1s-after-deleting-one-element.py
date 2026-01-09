class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''
        0,1,1,1,0,1,1,0,1
        max_sub = 0
        l, r = 0, 4

        count_0 = 2

        while count_0 > 1:
            if nums[l] == 0:
                count_0 -= 1
            
            l -= 1
        
        max_sub = max(max_sub, r-l)
        '''
        l, r = 0, 0
        count_0 = 0
        max_sub = 0
        while r < len(nums):
            if nums[r] == 0:
                count_0 += 1
            
            while count_0 > 1:
                if nums[l] == 0:
                    count_0 -= 1
                
                l += 1
            max_sub = max(max_sub, r - l)
            r += 1
        
        return max_sub