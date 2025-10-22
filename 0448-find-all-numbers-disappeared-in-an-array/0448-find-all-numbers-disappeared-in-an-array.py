class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_count = [0]*(len(nums)+1)

        for n in nums:
            nums_count[n] += 1
        res = []
        for i in range(1, len(nums)+1):
            if nums_count[i] == 0:
                res.append(i)
        return res
            