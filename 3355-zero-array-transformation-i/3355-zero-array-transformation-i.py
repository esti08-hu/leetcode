from typing import List 
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0]*(n+1)

        for l, r in queries:
            diff[l] +=1
            if r + 1 < n:
                diff[r+1]-=1
        pre = 0
        
        for i in range(n):
            pre+=diff[i]
            if nums[i] > pre:
                return False
        
        return True