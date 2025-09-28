class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(i, s):
            if i == len(nums):
                return 1 if s == target else 0
            if (i, s) in cache:
                return cache[(i, s)]

            add = dfs(i + 1, s + nums[i])
            subtract = dfs(i + 1, s - nums[i])
            cache[(i, s)] = add + subtract
            return cache[(i, s)]

        return dfs(0, 0)
