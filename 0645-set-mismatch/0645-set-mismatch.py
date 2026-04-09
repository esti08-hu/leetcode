class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_set = {i for i in range(1, len(nums)+1)}

        res = []
        for i in range(len(nums)):
            if nums[i] not in nums_set:
                res.append(nums[i])
            else:
                nums_set.remove(nums[i])
        
        res.append(nums_set.pop())
        return res