class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr, k):
            res.append(curr[:])
            if len(curr) == len(nums):
                return
            
            for i in range(k, len(nums)):
                curr.append(nums[i])
                backtrack(curr, i+1)
                curr.pop()

        backtrack([], 0)
        return res