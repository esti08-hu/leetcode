class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for acc in accounts:
            acc_sum = sum(acc)
            if acc_sum > max_wealth:
                max_wealth = acc_sum
        
        return max_wealth