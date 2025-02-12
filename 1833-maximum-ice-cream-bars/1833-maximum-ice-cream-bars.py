class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        max_cost = max(costs)
        
        count = [0] * (max_cost + 1)
        
        for cost in costs:
            count[cost] += 1

        total_bars = 0
        for cost in range(1, max_cost + 1):
            if count[cost] == 0:
                continue

            while count[cost] > 0 and coins >= cost:
                coins -= cost
                total_bars += 1
                count[cost] -= 1

        return total_bars
                