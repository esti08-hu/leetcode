class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for sell in prices[1:]:
            profit = max(profit, sell - buy)
            buy = min(buy, sell)
        
        return profit