class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        0 1 2 3 4 5 6 7 8 9 10 11
        '''
        if h < len(piles):
            return -1

        def can_finish(min_speed):
            hours = 0

            for pile in piles:
                hours+=math.ceil(pile/min_speed)

            return hours <= h

        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2

            if can_finish(mid):
                ans = mid
                high = mid
            else:
                low = mid + 1
        return low