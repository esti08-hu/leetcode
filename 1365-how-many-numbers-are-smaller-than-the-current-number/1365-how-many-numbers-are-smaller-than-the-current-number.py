class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            curr = 0
            for j in range(len(nums)):
                if nums[i] <= sorted_nums[j]:
                    res.append(curr)
                    break
                curr += 1
        
        return res