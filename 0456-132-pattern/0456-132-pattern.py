from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        min_i = nums[0]
        stk = []
        
        for j in range(1, len(nums)):
            while stk and nums[j] >= stk[-1][0]:
                stk.pop()
            
            if stk and nums[j] > stk[-1][1]:
                return True
            
            stk.append((nums[j], min_i))
            min_i = min(min_i, nums[j])
        
        return False