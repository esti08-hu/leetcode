class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums = Counter(nums)
        
        return ([k for k,v in nums.items() if v == 2])
    