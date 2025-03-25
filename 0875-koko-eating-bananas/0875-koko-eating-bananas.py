class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        def check(speed):
            hours = 0
            for pile in piles:
                hours+=-(-pile//speed)
            return hours <=h
        
        while low <= high:
            mid = (low + high) // 2

            if check(mid):
                high = mid-1
            else:
                low = mid + 1
        
        return low