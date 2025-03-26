class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        low, high = 1, max(ranks)*cars*cars

        def check(mid):
            summ = 0
            for r in ranks:
                summ += math.floor(math.sqrt(mid / r))
            return summ >= cars

        while low <= high:
            mid = (low + high) // 2

            if check(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low
