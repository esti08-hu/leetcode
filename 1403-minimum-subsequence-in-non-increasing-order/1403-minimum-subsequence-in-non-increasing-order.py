class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        curr = 0 
        total = sum(nums)

        for i in range(len(nums) - 1, -1, -1):
            curr += nums[i]
            res.append(nums[i])
            total -= nums[i]
            if curr > total:
                return res
        
        