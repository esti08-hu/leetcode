class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp =  {}
        max_len = 0
        for num in arr:
            prev_len = dp.get(num-difference, 0)
            dp[num] = prev_len + 1
            max_len = max(max_len, 1+prev_len)
        return max_len


