class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = float('inf')
        max_prof = 0

        for curr in prices:
            min_ = min(min_, curr)
            if curr > min_:
                max_prof += (curr - min_)
                min_ = curr
            
        return max_prof
            