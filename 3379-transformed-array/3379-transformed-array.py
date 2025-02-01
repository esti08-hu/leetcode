class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = []
        for i,n in enumerate(nums):
            indx = i + (n % len(nums))
            if indx >= len(nums):
                res.append(nums[indx%len(nums)])
            else:
                res.append(nums[indx])
        return res