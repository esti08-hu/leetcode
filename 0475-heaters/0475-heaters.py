class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def check(radius):
            heater_idx = 0
            for house in houses:
                while heater_idx < len(heaters) and heaters[heater_idx] + radius < house:
                    heater_idx += 1
                if heater_idx == len(heaters) or abs(heaters[heater_idx] - house) > radius:
                    return False
            return True

        left, right = 0, max(max(houses), max(heaters))
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1 

        return left
