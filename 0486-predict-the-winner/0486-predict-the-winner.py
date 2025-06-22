class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def dfs(start, end):
            if start == end:
                return nums[start]
            return max(nums[start] - dfs(start + 1, end), nums[end] - dfs(start, end - 1))
        return dfs(0, len(nums) - 1) >= 0