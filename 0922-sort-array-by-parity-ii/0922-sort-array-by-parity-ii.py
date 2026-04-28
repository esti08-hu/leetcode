class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        odd, even = 1, 0

        for i in range(len(nums)):
            if nums[i] % 2:
                res[odd] = nums[i]
                odd += 2
            else:
                res[even] = nums[i]
                even += 2
        
        return res
