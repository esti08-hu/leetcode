class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i = 0
        res = []
        while i < len(nums):
            for _ in range(nums[i]):
                res.append(nums[i+1])
            
            i += 2
        
        return res