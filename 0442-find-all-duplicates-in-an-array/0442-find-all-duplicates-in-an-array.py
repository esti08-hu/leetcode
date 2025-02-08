class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        check_dup = []
        res = []

        for i in range(len(nums)):
            if nums[i] not in check_dup:
                check_dup.append(nums[i])
            else:
                res.append(nums[i])
        return res