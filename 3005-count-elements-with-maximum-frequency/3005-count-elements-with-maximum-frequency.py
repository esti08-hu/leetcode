class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        return max(list(Counter(nums).values())) * list(Counter(nums).values()).count(max(list(Counter(nums).values())))
        
        
        # vals = list(Counter(nums).values())
        # max_val = max(vals)
        # count_max = vals.count(max_val)
        # return max_val * count_max