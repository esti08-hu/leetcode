class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        vals = list(Counter(nums).values())
        max_val = max(vals)
        count_max = vals.count(max_val)
        return max_val * count_max