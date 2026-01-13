class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        def dfs(idx, curr):
            if idx > len(nums):
                return

            if len(curr) > 1 and tuple(curr) not in seen:
                    res.append(curr[:])

            seen.add(tuple(curr))
            for i in range(idx, len(nums)):
                if not curr or curr[-1] <= nums[i]:
                    curr.append(nums[i])
                    dfs(i+1, curr)
                    curr.pop()
        dfs(0, [])
        return res